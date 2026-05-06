"""
매일 Yahoo Finance에서 주가·환율을 수집해 data/auto.json 을 갱신합니다.
"""
import json, datetime, pathlib
import yfinance as yf

ROOT = pathlib.Path(__file__).parent.parent
OUT  = ROOT / "data" / "auto.json"

TICKERS = {
    "005930.KS": {"name": "삼성전자",   "currency": "KRW"},
    "000660.KS": {"name": "SK하이닉스", "currency": "KRW"},
    "MU":        {"name": "Micron",      "currency": "USD"},
    "5713.T":    {"name": "Shin-Etsu",  "currency": "JPY"},
    "6727.T":    {"name": "SUMCO",       "currency": "JPY"},
}

FX_PAIRS = {
    "USDKRW": "KRW=X",
    "USDJPY":  "JPY=X",
}

def pct(current, prev):
    if prev and prev != 0:
        return round((current - prev) / prev * 100, 2)
    return None

def fetch_stocks():
    result = {}
    for ticker, meta in TICKERS.items():
        try:
            t = yf.Ticker(ticker)
            hist = t.history(period="2d")
            if len(hist) >= 1:
                price  = round(float(hist["Close"].iloc[-1]), 2)
                change = pct(price, float(hist["Close"].iloc[-2])) if len(hist) >= 2 else None
                result[ticker] = {**meta, "price": price, "change": change}
            else:
                result[ticker] = {**meta, "price": None, "change": None}
        except Exception as e:
            print(f"[WARN] {ticker}: {e}")
            result[ticker] = {**meta, "price": None, "change": None}
    return result

def fetch_fx():
    result = {}
    for pair, symbol in FX_PAIRS.items():
        try:
            t = yf.Ticker(symbol)
            hist = t.history(period="2d")
            if len(hist) >= 1:
                result[pair] = round(float(hist["Close"].iloc[-1]), 2)
            else:
                result[pair] = None
        except Exception as e:
            print(f"[WARN] {pair}: {e}")
            result[pair] = None
    return result

def main():
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = {
        "_updated": now,
        "_note": "자동 수집 데이터 (GitHub Actions). 수동 데이터는 manual.json 참조",
        "stocks": fetch_stocks(),
        "fx":     fetch_fx(),
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"✅ auto.json 업데이트 완료: {now}")
    for k, v in data["stocks"].items():
        chg   = f"{v['change']:+.2f}%" if v["change"] is not None else "N/A"
        price = str(v['price']) if v['price'] is not None else "N/A"
        print(f"  {v['name']:12s}  {price:>10}  {chg}")
    for k, v in data["fx"].items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()

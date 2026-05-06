# 🧠 메모리 반도체 투자 대시보드

AI 시대 메모리 반도체 시장을 추적하는 투자용 대시보드입니다.  
**매일 오전 9시(KST)** GitHub Actions가 주가·환율을 자동 수집합니다.

---

## 📂 파일 구조

```
├── index.html                     ← 대시보드 메인 페이지
├── data/
│   ├── auto.json                  ← 주가·환율 (Actions 자동 업데이트)
│   └── manual.json                ← 시장 점유율·가격·출하량 (직접 수정)
├── scripts/
│   └── fetch_data.py              ← 데이터 수집 스크립트
└── .github/workflows/
    └── update.yml                 ← 스케줄러
```

---

## 🚀 GitHub Pages 배포 (처음 한 번만)

### 1단계 — 저장소 생성 & 파일 업로드

```bash
# 터미널에서 실행
git init
git add .
git commit -m "init: 메모리 반도체 대시보드"
git remote add origin https://github.com/YOUR_USERNAME/memory-dashboard.git
git push -u origin main
```

### 2단계 — GitHub Pages 활성화

1. 저장소 → **Settings** → 좌측 **Pages**
2. **Source** → `Deploy from a branch`
3. **Branch** → `main` / `/ (root)` 선택
4. **Save** 클릭
5. 1~2분 후 `https://YOUR_USERNAME.github.io/memory-dashboard` 접속

### 3단계 — GitHub Actions 권한 설정

1. 저장소 → **Settings** → **Actions** → **General**
2. **Workflow permissions** → `Read and write permissions` 선택
3. **Save**

---

## 🔄 데이터 업데이트 방법

### 자동 (매일 오전 9시 KST)
- 삼성전자, SK하이닉스, Micron, Shin-Etsu, SUMCO 주가
- USD/KRW, USD/JPY 환율

수동으로 즉시 실행하려면:  
저장소 → **Actions** → `매일 시장 데이터 자동 업데이트` → **Run workflow**

### 수동 (분기 1회 권장)
`data/manual.json` 파일을 GitHub 웹에서 직접 편집합니다.

**업데이트 시기:**
| 데이터 | 업데이트 시기 | 참고 소스 |
|--------|-------------|---------|
| DRAM/NAND 점유율 | 분기별 | TrendForce, Counterpoint |
| 가격 트렌드 | 분기별 | TrendForce, Sourceability |
| 웨이퍼 출하량 | 분기별(SEMI 발표 후) | semi.org |
| 시장 규모 | 연간 | Statista, SkyQuest |

**manual.json 웹 편집 방법:**
1. GitHub에서 `data/manual.json` 클릭
2. ✏️ (연필 아이콘) 클릭
3. 값 수정 후 **Commit changes**

---

## 📊 주요 추적 지표

| 지표 | 설명 |
|------|------|
| 삼성전자 (005930.KS) | DRAM/NAND 최대 제조사 |
| SK하이닉스 (000660.KS) | HBM 세계 1위 (70% 점유) |
| Micron (MU) | 미국 유일 DRAM 제조사 |
| Shin-Etsu (5713.T) | 웨이퍼 세계 1위 |
| SUMCO (6727.T) | 웨이퍼 세계 2위 |

---

> ⚠️ 투자 참고용 정보입니다. 투자 결정은 본인 판단 하에 진행하세요.

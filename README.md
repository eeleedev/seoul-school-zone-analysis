# Seoul School Zone Analysis
## 디렉토리 구조
```
.
├── README.md                # 프로젝트 개요, 실행 방법, 주요 결과 요약
├── .gitignore               # Git에서 추적하지 않을 파일/폴더 목록 (대용량 데이터, 가상환경 등)
├── data/
│   ├── processed/           # 전처리된 데이터
│   ├── interim/             # 중간 결과물 데이터
│   └── additional/          # 추가 데이터
├── notebooks/               # Jupyter Notebooks
│   └── EDA/                 # EDA 관련 노트북들을 모아둘 하위 폴더
├── reports/                 # 최종 분석 보고서 (docx, PDF 등)
│   └── figures/             # 보고서에 사용된 이미지, 플롯
└── references/              # 참고 문서 (공개 가능한 참고 문서)
```


## 커밋 메시지 컨벤션 (Commit Message Convention)

### 타입 (Type):
- feat: 새로운 분석 기능 추가 (EDA, 모델링, 시각화 등)
- fix: 분석 코드 또는 데이터 처리 과정의 오류 수정
- docs: README, 분석 보고서, 주석 등 문서 수정
- style: 코드 포맷팅, 세미콜론 누락 등 (분석 결과에 영향 없는 스타일 변경)
- refactor: 분석 결과 변경 없이 코드 구조 개선
- chore: 빌드 스크립트, 패키지 매니저 설정 등 기타 잡일 (라이브러리 추가 등)
- data: 데이터셋 추가, 변경, 전처리 스크립트 수정 (데이터 자체의 변경이나 그와 관련된 스크립트)
- viz: 시각화 관련 코드 추가 또는 수정
- report: 분석 결과 보고서 내용 추가 또는 수정

### 스코프 (Scope)
커밋 변경의 영향 범위
- eda
- preprocessing
- modeling
- visualization
- data-cleaning

### 커밋 메시지 예시: 
현재 시제로 명확하고 간결하게 작성 (50자 이내 권장). 문장 끝에 마침표는 찍지 않음.
- [feat(eda)] Add distribution plots for key features
- [fix(preprocessing)] Handle missing values in sales_data.csv
- [docs] Update README with setup instructions
- [data] Add new customer survey data from Q1 2025
- [viz(report)] Improve clarity of monthly sales trend chart

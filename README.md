# Seoul School Zone Analysis
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

### 제목 (Subject): 
현재 시제로 명확하고 간결하게 작성 (50자 이내 권장). 문장 끝에 마침표는 찍지 않음.

**예시**
- feat(eda): Add distribution plots for key features
- fix(preprocessing): Handle missing values in sales_data.csv
- docs: Update README with setup instructions
- data: Add new customer survey data from Q1 2025
- viz(report): Improve clarity of monthly sales trend chart

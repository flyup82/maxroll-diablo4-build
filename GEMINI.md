# 프로젝트 규칙 및 자율 작업 일지 (GEMINI.md)

본 문서는 디아블로 IV 빌드 분석 프로젝트 레벨의 규칙 명세이자, 에이전트의 단기 기억을 복원하는 자율 작업 기록(Traceability Log)입니다.

---

## 1. 프로젝트 전용 규칙 (Project Rules)

### 1.1. 정책 참조 체인 (Policy Reference Chain)
에이전트는 작업 수행 시 아래 정의된 프로젝트 내부/외부 표준 명세서를 최우선 참조합니다.
*   **코딩 표준 및 번역 사전**: [.agents/rules/instructions.md](file://./.agents/rules/instructions.md)
*   **Maxroll 범용 빌드 가이드 생성 글로벌 프로세스**: [.agents/global_maxroll_guide_generation_prompt.md](file://./.agents/global_maxroll_guide_generation_prompt.md)
*   **디아블로 4 핵심 메커니즘 및 파밍 지식 베이스**: [.agents/rules/d4_knowledge_base.md](file://./.agents/rules/d4_knowledge_base.md)

### 1.2. 추론 노력 배분 정책 (Reasoning Effort Guidelines)
에이전트는 작업 성격에 맞추어 모델의 추론 노력을 적절히 배분하여 리소스를 최적화합니다.
*   **Low / Medium Effort**: 단순 HTML 파싱/크롤링 구동, 마크다운 문서 편집, 단순 리팩토링.
*   **High Effort**: SVG 로드맵 레이아웃 갱신, 복잡한 CSS 반응형 차트 수정, 템플릿 변환 규칙 개편.

### 1.3. 강조 CSS 클래스 매핑 규칙
최종 HTML 결과물 빌드 시 아래 등급별 CSS 속성을 정확히 태그에 적용해야 합니다:
- 위상 (Aspect): `.h-aspect` (주황색, 박스 없음)
- 룬 (Rune): `.h-rune` (녹색, 박스 없음)
- 고유 (Unique): `.h-unique` (골드색, 박스 없음)
- 신화 (Mythic): `.h-mythic` (연보라색, 박스 없음)
- 스킬 (Skill): `.h-skill` (하늘색, 박스 없음)
- 문양 (Glyph): `.h-glyph` (오렌지색, 문양 SVG 아이콘 결합, 박스 없음)
- 정복자 판 (Paragon): `.h-paragon` (금노랑, 정복자 격자 SVG 아이콘 결합, 박스 없음)
- 일반/상태이상 (General/Status): `.h-general` (하늘색, 박스 없음)

---

## 2. 프로젝트 추적 로그 (Traceability Log)

### 2.1. 작업 트리 현황 (Task Tree)
*   [x] **1단계: 초기화**: agy-init 및 디아블로 4 전용 크롤러/규칙 탑재 완료.
*   [x] **2단계: 구현**: 심장추적자 도적 시즌 14 마크다운/HTML 분석 완료.
*   [x] **3단계: 가시화**: 반응형 CSS/SVG 기반의 로드맵 차트 개발 완료.
*   [x] **4단계: 최적화**: 룰셋 명명 규칙 및 위상 분리 리팩토링 및 2차 PR 제출 완료.
*   [x] **5단계: 표준화**: Mermaid 구문 에러 해결, 얇은 간트 차트 UI 개선, 시즌 6+ 스케일 패치, 공용 UI 마스터 템플릿화 완료.
*   [x] **6단계: 확장**: 화살비 도적 시즌 14 가이드 분석 및 한글화 렌더링 완료.
*   [x] **7단계: 정책 고도화**: 특정 빌드에 국한되지 않는 Maxroll 범용 빌드 가이드 생성 글로벌 프로세스(Global Policy) 수립 및 탑재 완료.
*   [x] **8단계: 자동화 실증**: 방패 돌진 성기사(Shield Charge Paladin) 가이드를 타겟으로 신규 글로벌 프로세스 기반 자동 분석 및 산출물(Markdown, HTML) 렌더링 성공.

### 2.2. 작업 타임라인 및 마일스톤 (Milestones)
*   **2026-07-11**: 프로젝트 신규 세팅 완료.
*   **2026-07-11**: 심장추적자 도적 시즌 14 빌드 원본 분석 및 한글 정식 용어집 정밀 대조 완료.
*   **2026-07-11**: 마크다운 가이드(`heartseeker_rogue_guide.md`) 및 프리미엄 다크테마 HTML 가이드(`heartseeker_rogue_guide.html`) 생성 완료.
*   **2026-07-11**: HTML 내 강조 색상 스키마 세분화 완료.
*   **2026-07-11**: HTML 파밍 루트 하단에 반응형 로드맵 타임라인 차트(CSS + SVG) 개발 완료.
*   **2026-07-11**: 규칙 네이밍 모범 관행 최적화 및 `instructions.md` / `GEMINI.md` 위상 분리 리팩토링 및 신규 PR(#19) 갱신 완료.
*   **2026-07-11**: Mermaid 구문 에러 수정, 얇고 오밀조밀한 간트 차트 UI 리뉴얼, 시즌 6+ 1-60 및 Paragon 1-300 축 적용 완료.
*   **2026-07-11**: 클래스명 기반 멀티 빌드 명명 규격(`[class]_[build]_guide`) 정립 및 마스터 공용 UI HTML 템플릿(`templates/build_guide_template.html`) 배포 완료.
*   **2026-07-11**: 번역기 로컬 깃 레포(`ffext-Maxroll-diablo4-translator`)를 분석하여 용어 정규화 완료 (닐푸르의 좁은 눈 ➜ **찌푸린 눈**, 체 ➜ **세흐**, 시르세 ➜ **시르세흐**).
*   **2026-07-11**: 룬(Rune)과 참(Charm)의 등급 명칭 색상을 각각 Gold(`#ffbf00`) 및 Green(`#10b981`)으로 Maxroll 사양에 동기화 완료.
*   **2026-07-11**: HTML 빌드 개요 부분에 반응형 CSS/SVG Flowchart 구조 다이어그램 적용 완료.
*   **2026-07-11**: 한글 번역기 데이터셋(`aspects.json`, `uniques.json`, `skills.json`, `glyphs.json`, `horadric-component.json`, `board.json` 등)을 워크스페이스 로컬 `.agents/rules/d4_translator_data/` 에 통째로 영구 이식 완료.
*   **2026-07-11**: 화살비 도적 시즌 14 빌드 원본 분석 및 한글 정식 용어집 정밀 매핑 완료.
*   **2026-07-11**: 화살비 도적 전용 마크다운 가이드(`rogue_rain_of_arrows_guide.md`) 및 프리미엄 다크테마 HTML 가이드(`rogue_rain_of_arrows_guide.html`) 생성 완료.
*   **2026-07-20**: Playwright 소켓 에러 관련 예측/테스트 결과 및 Antigravity 차단 버그 피드백 문서 생성 및 프로젝트 루트 배치 완료.
*   **2026-08-03**: 특정 직업에 제한되지 않는 Maxroll 범용 빌드 가이드 생성 프롬프트(`.agents/global_maxroll_guide_generation_prompt.md`) 수립 및 프로젝트 정책 참조 체인(Policy Reference Chain)에 자동 연동. (이후 모든 Maxroll 빌드 URL 요청 시 본 프로세스 강제 적용)
*   **2026-08-03**: 글로벌 프로세스 적용 실증 테스트 - 방패 돌진 성기사 빌드 마크다운(`260803_140000_shield_charge_paladin_guide.md`) 및 마스터 템플릿 기반 HTML 가이드(`260803_140000_shield_charge_paladin_guide.html`) 생성 완료 (시즌 14 1-70 스케일 강제 적용).
*   **2026-08-03**: `analyze_build.py` 로직 개편 및 지식 베이스(d4_knowledge_base)를 반영하여 방패 돌진 성기사 가이드 V2 재출력 완료 (`260803_145800_shield_charge_paladin_guide.[md|html]`).
*   **2026-08-03**: `analyze_build.py`의 과도한 참(Charm) 분류 휴리스틱 버그(ex: `of the`)를 수정하여 고유 장비("회색의 어깨걸이" 등)가 녹색 부적으로 오분류되는 문제 해결 및 V3 재출력 완료 (`260803_150700_shield_charge_paladin_guide.[md|html]`).
*   **2026-08-03**: 외부 블로그 교차 검증을 통해 시즌 14 신규 보스(증오의 사도, 아스타로트 등) 타겟 드랍 테이블 갱신 (지식 베이스 업데이트). 이를 반영하여 방패 돌진 성기사 V4 재출력 완료 (`260803_151600_shield_charge_paladin_guide.[md|html]`).
*   **2026-08-03**: 응보의 방패 성기사 레벨링 가이드 마크다운(`260803_151700_shield_of_retribution_paladin_leveling_guide.md`) 및 마스터 템플릿 기반 HTML 가이드(`260803_151700_shield_of_retribution_paladin_leveling_guide.html`) 생성 완료.


### 2.3. 핵심 설계 결정 사항 (Architectural Decisions)
*   **규칙의 계층화 격리**:
    *   **글로벌 룰 (`GEMINI.md`)**: 에이전트의 보편적인 코딩 및 프로젝트 자율 초기화/추적 규칙만 전역 주입.
    *   **로컬 룰 (`GEMINI.md` 및 `instructions.md`)**: 디아블로 4 전용 용어 사전 및 렌더링 강조 CSS 스키마를 로컬로 완전히 격리.
*   **빌드 가이드의 UI 일관성 템플릿화**:
    *   에이전트 변경과 무관하게 통일성 있는 UI 품질 보존을 위해 `templates/build_guide_template.html`을 복제하여 가이드 HTML을 생성하도록 마스터 템플릿 체계를 이식함.


### 2.4. 현재 장애물 및 종속성 (Blockers)
*   터미널 샌드박스의 일시적인 소켓 연결 해제 현상 (가이드 파일의 수동 정리 권장).

### 2.5. 다음 작업 인계사항 (Next Steps)
*   추가적인 디아블로 4 빌드 가이드 분석 또는 템플릿 적용 요구사항 대기 중.



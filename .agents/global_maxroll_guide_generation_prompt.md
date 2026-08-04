# Maxroll Diablo IV 범용 빌드 가이드 생성 프롬프트 및 프로세스 (Global Policy)

**[목적]**
이 프롬프트는 에이전트가 특정 직업에 국한되지 않고, Maxroll의 모든 디아블로 IV 빌드 가이드(레벨링, 엔드게임 등) URL을 입력받아 프로젝트 표준 마크다운(Markdown) 및 HTML 공략본으로 자동 변환하기 위한 글로벌 정책 프로세스입니다.

---

## 1. 초기 인입 및 데이터 파싱 (Build Analysis & Data Collection)
**작업 내용:** 입력된 `[MAXROLL_BUILD_URL]`에서 아래의 공통 및 직업/시즌 특화 요소들을 모두 누락 없이 추출하여 구조화합니다.
**수집 항목 체크리스트:**
*   **Overview & Pros/Cons:** 빌드 핵심 요약, 장점 및 단점.
*   **Skill Tree & Progression:** 레벨링 구간(1-70) 스킬 포인트 투자 순서 및 최종 스킬 트리.
*   **Gameplay & Rotation:** 기본 사냥법, 딜 사이클(Rotation), 생존기 및 쿨타임 관리법.
*   **Class Specific Mechanics:** 직업 고유 메커니즘 (도적: 전문화 / 야만용사: 무기 기예 / 원소술사: 마법부여 / 강령술사: 망자의 서 / 드루이드: 영혼 은총 / 혼령사: 혼령 전당 등).
*   **Gearing & Stats:** 부위별 추천 장비, 주요 옵션(Stats) 우선순위. **반드시 각 고유/신화 아이템 및 룬/문양의 주요 획득처(드랍 보스, 필요 재료 등) 정보를 포함할 것.**
*   **Legendary Aspects & Uniques:** 추천 위상(힘의 전서 포함), 고유 및 신화 아이템.
*   **Runewords & Gems:** 시즌 특화 룬어(Runewords) 조합 및 부위별 보석 세팅.
*   **Mercenaries:** (시즌 6+ 이후 공통) 주 용병(Hired) 및 증원(Reinforcement) 세팅.
*   **Paragon Board:** 정복자 보드 진행 순서 및 문양(Glyphs) 배치.
*   **Roadmap / Progression:** 단계별 빌드업 목표 및 타임라인.

## 2. 공식 번역 데이터베이스 연동 및 용어 정규화 (Translation & Normalization)
**작업 내용:** 추출된 영문 텍스트를 프로젝트 내부의 SSOT(Single Source of Truth) JSON 데이터를 바탕으로 한글 클라이언트 정식 용어로 100% 매핑합니다.
*   **데이터 출처 (Source):** 워크스페이스 내 `.agents/rules/d4_translator_data/` 디렉토리 (원본: `ffext-Maxroll-diablo4-translator` 저장소 기반 최신화 파일).
*   **매핑 대상:** `aspects.json`(위상), `uniques.json`(고유/신화), `skills.json`(스킬/수동태), `horadric-component.json`(룬/참), `glyphs.json`(문양), `board.json`(정복자).

## 3. 중간 마크다운 생성 및 치환 준비 (Markdown Generation)
**작업 내용:** 정규화된 데이터를 바탕으로 각 섹션별 마크다운 초안을 작성합니다. HTML 변환 시 CSS 적용을 위해 아래의 강조 규칙을 준수하여 렌더링 태그를 적용합니다.
*   **CSS 클래스 매핑 규칙:**
    *   위상: `.h-aspect` (주황색) | 고유: `.h-unique` (밝은 골드색 `#DCA779`) | 신화: `.h-mythic` (연보라색)
    *   룬: `.h-rune` (금색) | 스킬: `.h-skill` (하늘색) | 문양: `.h-glyph` (오렌지색)
    *   정복자 보드: `.h-paragon` (금노랑) | 일반/상태이상/직업메커니즘: `.h-general` (하늘색)
    *   (주의: `analyze_build.py`가 추출된 텍스트에 등장하는 용어만 100% 필터링하여 프롬프트에 제공하므로, 반드시 프롬프트 내에 기재된 사전을 참조할 것)

## 4. 마스터 템플릿 로드 및 HTML 렌더링 (Template Application)
**작업 내용:** 공용 마스터 템플릿(`templates/build_guide_template.html`)을 복제한 뒤, 마크다운의 내용을 아래 주요 영역 치환자(Placeholder)에 주입합니다.
*   **`{{OVERVIEW_HTML}}`**: 빌드 개요, 장단점, 직업 고유 메커니즘, 용병 세팅 등.
*   **`{{GAMEPLAY_HTML}}`**: 스킬 트리, 딜 사이클, 사냥법 텍스트 및 Flowchart.
*   **`{{REQUIREMENTS_HTML}}`**: 장비(위상, 고유), 룬어, 보석, 주요 스탯. **반드시 이 영역 하단에 고유 아이템, 룬, 문양 등을 얻기 위한 주요 보스 타겟 파밍 테이블 및 필요 재료 팁(Acquisition & Tips)을 요약하여 표기할 것.**
*   **`{{FARMING_SUMMARY_TABLE_HTML}}`**: 단계별 파밍 요약표.
*   **`{{GANTT_ROWS_HTML}}`**: 하위 5번 항목의 로드맵 간트 차트 코드가 삽입되는 영역.

## 5. 로드맵 차트 및 타임라인 최적화 (Season 14+ Optimization)
**작업 내용:** 시즌 14 기준의 최신 육성 타임라인을 반영하여 얇고(18px) 오밀조밀한(0.75rem 간격) 간트 차트를 생성합니다.
*   **최신 타임라인 스케일 (시즌 14 기준):**
    *   **Starter:** 레벨 1 - 70 (시즌 14 레벨업 구간 반영)
    *   **Early:** 정복자(Paragon) 1 - 100
    *   **Mid:** 정복자 100 - 200
    *   **Late / Push:** 정복자 200 - 300 (시즌 14 최신 정복자 한도 기준)

## 6. 최종 산출물 저장 (File Generation & Traceability)
**작업 내용:** 모든 렌더링이 끝난 결과물을 **반드시 아래의 타임스탬프 명명 규칙**에 따라 프로젝트 루트에 저장합니다.
*   **출력 파일명 명명 규칙:** `YYMMDD_hhmmss_[빌드명]_[문서종류(guide)].[확장자]`
    *   예시 (마크다운): `260803_135020_blizzard_sorcerer_guide.md`
    *   예시 (HTML): `260803_135020_blizzard_sorcerer_guide.html`
*   **로그 업데이트:** 작업 완료 후 프로젝트 루트의 `GEMINI.md` [Traceability Log] 섹션에 해당 빌드 공략 가이드 생성 이력을 간략히 기록합니다.

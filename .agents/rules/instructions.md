# 에이전트 코딩 및 행동 지침서 (Agent Instructions)

이 프로젝트 워크스페이스 내에서 코드를 수정하거나 추가하는 모든 에이전트는 아래 지침을 엄격히 준수합니다.

## 1. 코드 품질 및 아키텍처 규칙
*   **단일 책임 원칙 (SRP)**: 클래스와 함수는 단 하나의 역할만 수행하도록 작게 분할합니다.
*   **관심사 분리 (SoC)**: 비즈니스 로직, 데이터 수집(Crawler 등), UI 렌더링 영역은 파일 단위로 완벽히 격리합니다.
*   **의존성 최소화**: 외부 패키지 설치 시 사전에 사용자 승인을 얻고, 가급적 표준 라이브러리(Standard Library)를 활용합니다.

## 2. 보안 경계 (Security Boundaries)
*   **자격 증명 노출 금지**: API Key, 토큰, 비밀번호 등의 시크릿 정보는 절대 소스코드에 하드코딩하지 않습니다. `.env` 파일과 환경 변수를 활용하고, 해당 파일이 `.gitignore`에 등록되어 있는지 반드시 확인합니다.
*   **권한 남용 방지**: 시스템 환경에 쓰기 작업을 수행하거나 외부 패키지 설치 시 `run_command` 실행 전에 보안 리스크를 자체 검토합니다.

## 3. 테스트 및 검증 규칙
*   **빌드 무결성**: 코드 수정 완료 후, 반드시 컴파일 또는 린트(Lint) 도구를 실행하여 구문 오류가 없는지 자율 검증합니다.
*   **기존 테스트 준수**: 워크스페이스 내에 기존 단위 테스트가 존재할 경우, 변경 사항이 이를 통과하는지 검증 후 보고합니다.

## 4. 커밋 및 문서화 규격
*   **Conventional Commits**: 커밋 메시지는 `feat:`, `fix:`, `refactor:`, `docs:` 등의 접두사를 사용하여 명료하게 작성합니다.
*   **도큐멘테이션 유지**: 코드 내 기존 docstring 및 핵심 아키텍처 주석은 임의로 지우거나 변형하지 않습니다.

---

## 5. 프로젝트 전용 규칙: 공식 번역 데이터베이스 연동 및 정규화
디아블로 IV 빌드를 분석하거나 번역 문서를 작성할 때, 임의 번역이나 수동 사전을 사용하지 말고 로컬에 적재된 `.agents/rules/d4_translator_data/` 디렉토리 내의 공식 번역 JSON 데이터베이스를 SSOT(Single Source of Truth)로 삼아 모든 명칭을 100% 매핑하여 적용해야 합니다.
*   **적용 대상 사전**:
    *   위상 번역: `d4_translator_data/aspects.json` 및 `aspects_inven.json`
    *   고유/신화 번역: `d4_translator_data/uniques.json`
    *   스킬/효과 번역: `d4_translator_data/skills.json`
    *   룬/참 번역: `d4_translator_data/horadric-component.json` (예: `Cir` ➜ 시르, `Ceh` ➜ 세흐, `Narrow Eye` ➜ 찌푸린 눈)
    *   정복자 보드 번역: `d4_translator_data/board.json`
    *   문양 번역: `d4_translator_data/glyphs.json`


## 6. 출력 파일명 명명 규칙 (Multi-Build Output Naming)
새로운 빌드의 분석 또는 번역 문서를 작성하여 저장할 때, 다음과 같이 클래스명과 빌드명을 기반으로 소문자 언더스코어 조합의 파일명을 생성하십시오:
*   **Markdown 가이드**: `[class]_[build_name]_guide.md`
*   **HTML 보고서**: `[class]_[build_name]_guide.html`
*   **예시**:
    *   도적 심장추적자: `rogue_heartseeker_guide.md` / `rogue_heartseeker_guide.html`
    *   도적 화살비: `rogue_rain_of_arrows_guide.md` / `rogue_rain_of_arrows_guide.html`
    *   드루이드 칼날발톱: `druid_shred_guide.md` / `druid_shred_guide.html`

## 7. 공용 UI 템플릿 준수 규칙
일관성 있는 빌드 리포트 품질 보존을 위해, 모든 HTML 출력물은 반드시 `templates/build_guide_template.html`을 복제하여 본문 영역(`{{OVERVIEW_HTML}}`, `{{GAMEPLAY_HTML}}`, `{{REQUIREMENTS_HTML}}`, `{{GANTT_ROWS_HTML}}`, `{{FARMING_SUMMARY_TABLE_HTML}}` 등)만 교체하여 생성합니다.
*   **로드맵 간트 차트 디자인 사양**:
    *   막대(`.gantt-bar`) 높이는 **18px**로 얇게 유지하고, 행 간 간격(`.gantt-grid`)은 **0.75rem**으로 오밀조밀하게 붙여 세련되게 렌더링합니다.
    *   시간선 축(Scale)은 이전의 100레벨 초과 구조가 아닌, **Diablo IV 시즌 6+ 기준**에 맞춰 다음과 같이 매핑합니다:
        *   **Starter**: 캐릭터 레벨 1 - 60
        *   **Early**: 정복자 레벨 1 - 100 (Torment 1 정착)
        *   **Mid**: 정복자 레벨 100 - 200 (Torment 2-3 정착)
        *   **Late / Push**: 정복자 레벨 200 - 300 (Torment 4 및 고단 푸시)


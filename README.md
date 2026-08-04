# 🏹 디아블로 IV 빌드 분석 파이프라인 (D4 Build Analyzer)

`[License: MIT]` `[Python: 3.9+]` `[Gemini: Native]`

Maxroll.gg의 디아블로 IV endgame 빌드 가이드를 크롤링하여 태그를 정제하고, 정밀한 AI 기계 번역과 수식 시각화를 적용하여 프리미엄 한국어 분석 리포트를 제작하는 지능형 워크스페이스입니다.

---

## ✨ 핵심 특장점 (Key Features)

*   ⚡ **클린 텍스트 파싱**: maxroll.gg URL에서 광고, 불필요한 스크립트 및 HTML 보일러플레이트를 걸러내어 AI가 분석하기 좋은 핵심 지문 추출.
*   📜 **동적(Dynamic) 용어 매핑**: 게임 내 한국어 공식 명칭(위상/스킬/고유 아이템 등)을 크롤링한 영문 텍스트 내 존재 여부를 확인하여 100% 매칭 및 할루시네이션 방지.
*   🧠 **D4 지식 베이스 연동**: 시즌별 최신 보스 드랍 테이블(증오의 사도, 아스타로트 등)과 게임 메커니즘을 정의한 `.agents/rules/d4_knowledge_base.md`를 기반으로 파밍 가이드라인 자동 생성.
*   🎨 **글로벌 템플릿화 및 시각적 차트**: 특정 빌드에 국한되지 않는 범용 프롬프트(`.agents/global_maxroll_guide_generation_prompt.md`)와 공통 HTML 템플릿을 통해 일관된 반응형 간트 차트 및 다이어그램 시각화.

---

## 🛠️ 기술 스택 (Tech Stack)

*   **Language**: Python 3.9+ (BeautifulSoup4 / urllib)
*   **Runtime Engine**: Google Antigravity Agent Framework
*   **Output Engine**: Responsive HTML5 & CSS3 / Github-Flavored Markdown

---

## 📥 입출력 인터페이스 (Input & Output Interface)
*   **입력**: Maxroll.gg 특정 빌드 가이드 URL.
*   **산출 아티팩트**: `[클래스명]_[빌드명]_guide.md` (마크다운) 및 `[클래스명]_[빌드명]_guide.html` (HTML 보고서) 파일.

---

## 🏃 퀵 스타트 (Quick Start)

### 1단계: 프로젝트 초기화
```bash
# 새로운 폴더에서 하네스 명령을 사용해 초기화합니다.
mkdir my-new-project && cd my-new-project
agy-init
```

### 2단계: 분석 스크립트 구동
```bash
python3 analyze_build.py [maxroll_build_url]
```

### 3단계: AI 번역 및 리포트 자동 생성
*   `analyze_build.py`를 실행하면 `prompt_for_ai.txt`가 자동 생성됩니다.
*   글로벌 정책 프롬프트 및 지식 베이스를 바탕으로 AI 에이전트가 `[클래스명]_[빌드명]_guide.md` 및 `.html` 가이드를 템플릿 기반으로 렌더링하여 프로젝트 폴더 내에 저장합니다.

---

## 🤝 기여 방법 (Contributing)
이슈(Issues) 등록 및 풀 리퀘스트(Pull Requests)는 언제나 환영합니다! 기여 절차에 대한 상세 사항은 `CONTRIBUTING.md`를 참고해 주세요.

## 📄 라이선스 (License)
본 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

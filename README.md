# 🏹 디아블로 IV 빌드 분석 파이프라인 (D4 Build Analyzer)

`[License: MIT]` `[Python: 3.9+]` `[Gemini: Native]`

Maxroll.gg의 디아블로 IV endgame 빌드 가이드를 크롤링하여 태그를 정제하고, 정밀한 AI 기계 번역과 수식 시각화를 적용하여 프리미엄 한국어 분석 리포트를 제작하는 지능형 워크스페이스입니다.

---

## ✨ 핵심 특장점 (Key Features)

*   ⚡ **클린 텍스트 파싱**: maxroll.gg URL에서 광고, 불필요한 스크립트 및 HTML 보일러플레이트를 걸러내어 AI가 분석하기 좋은 핵심 지문 추출.
*   📜 **공식 용어 완벽 매핑**: 게임 내 한국어 공식 명칭과 위상/스킬 명칭을 100% 매칭하는 에이전트 번역 가이드 탑재.
*   🎨 **시각적 로드맵 차트**: HTML 보고서 하단에 반응형 CSS 및 SVG 기반의 레벨링/아이템 파밍 가이드라인 타임라인 시각화 적용.

---

## 🛠️ 기술 스택 (Tech Stack)

*   **Language**: Python 3.9+ (BeautifulSoup4 / urllib)
*   **Runtime Engine**: Google Antigravity Agent Framework
*   **Output Engine**: Responsive HTML5 & CSS3 / Github-Flavored Markdown

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

### 3단계: AI 번역 및 리포트 저장
*   생성된 `prompt_for_ai.txt` 파일을 복사하여 Gemini에 전달합니다.
*   출력된 Markdown 소스를 `heartseeker_rogue_guide.md`로, HTML 소스를 `heartseeker_rogue_guide.html`로 저장합니다.

---

## 🤝 기여 방법 (Contributing)
이슈(Issues) 등록 및 풀 리퀘스트(Pull Requests)는 언제나 환영합니다! 기여 절차에 대한 상세 사항은 `CONTRIBUTING.md`를 참고해 주세요.

## 📄 라이선스 (License)
본 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

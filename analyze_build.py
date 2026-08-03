#!/usr/bin/env python3
import sys
import os
import json
import re
import urllib.request
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = []
        self.in_script = False
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.in_script = True
        elif tag == 'style':
            self.in_style = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
        elif tag == 'style':
            self.in_style = False

    def handle_data(self, d):
        if not self.in_script and not self.in_style:
            self.text.append(d)

    def get_data(self):
        return ''.join(self.text)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# Dynamic Dictionary Loader
def load_localization_db():
    rules_dir = ".agents/rules/d4_translator_data"
    if not os.path.exists(rules_dir):
        # Fallback to absolute path just in case
        rules_dir = "/home/flyup82/_AIs_Antigravity/maxroll_dia4_build/.agents/rules/d4_translator_data"
    
    aspects = {}
    uniques = {}
    skills = {}
    glyphs = {}
    components = {}
    board = {}

    try:
        with open(os.path.join(rules_dir, "aspects.json"), "r", encoding="utf-8") as f:
            aspects = json.load(f)
        with open(os.path.join(rules_dir, "uniques.json"), "r", encoding="utf-8") as f:
            uniques = json.load(f)
        with open(os.path.join(rules_dir, "skills.json"), "r", encoding="utf-8") as f:
            skills = json.load(f)
        with open(os.path.join(rules_dir, "glyphs.json"), "r", encoding="utf-8") as f:
            glyphs = json.load(f)
        with open(os.path.join(rules_dir, "horadric-component.json"), "r", encoding="utf-8") as f:
            components = json.load(f)
        with open(os.path.join(rules_dir, "board.json"), "r", encoding="utf-8") as f:
            board = json.load(f)
    except Exception as e:
        print(f"[Warning] Failed to load local translator database files: {e}", file=sys.stderr)
        
    return {
        "aspects": aspects,
        "uniques": uniques,
        "skills": skills,
        "glyphs": glyphs,
        "components": components,
        "board": board
    }

def build_glossary_prompt(db, text):
    text_lower = text.lower()
    # Classify components (Runes vs Charms) and uniques (Mythic vs Unique)
    aspect_rules = []
    rune_rules = []
    charm_rules = []
    unique_rules = []
    mythic_rules = []
    skill_rules = []
    glyph_rules = []
    paragon_rules = []

    def is_in_text(en):
        return en.lower() in text_lower

    # Aspects Mapping
    for en, ko in db["aspects"].items():
        if is_in_text(en):
            aspect_rules.append(f"   - {en} -> {ko}")

    # Skills Mapping
    for en, ko in db["skills"].items():
        if is_in_text(en):
            skill_rules.append(f"   - {en} -> {ko}")

    # Glyphs Mapping
    for en, ko in db["glyphs"].items():
        if is_in_text(en):
            glyph_rules.append(f"   - {en} -> {ko}")

    # Paragon Board Mapping
    for en, ko in db["board"].items():
        if is_in_text(en):
            paragon_rules.append(f"   - {en} -> {ko}")

    # Uniques & Mythics classification
    mythic_keywords = ["harlequin", "shroud of false", "starless", "tyrael", "perdition", "melted", "doombringer", "grandfather"]
    for en, ko in db["uniques"].items():
        if is_in_text(en):
            is_mythic = any(kw in en.lower() for kw in mythic_keywords)
            if is_mythic:
                mythic_rules.append(f"   - {en} -> {ko}")
            else:
                is_charm = "charm" in en.lower()
                if is_charm:
                    charm_rules.append(f"   - {en} -> {ko}")
                else:
                    unique_rules.append(f"   - {en} -> {ko}")

    # Horadric Components (Runes) classification
    for en, ko in db["components"].items():
        if is_in_text(en):
            if len(en) <= 4 or "rune" in en.lower():
                rune_rules.append(f"   - {en} -> {ko}")
            else:
                is_charm = "charm" in en.lower()
                if is_charm:
                    charm_rules.append(f"   - {en} -> {ko}")

    # Build the structured markdown guide
    glossary = f"""[디아블로 IV 공식 한글 용어 번역 및 HTML 강조 가이드라인 (동적 연동 DB)]

AI는 번역 및 가이드 문서 작성 시 다음 용어들을 반드시 한국어 공식 명칭으로 번역하고, HTML 출력물에서는 각 용어 속성에 알맞은 <span> 클래스로 감싸주어야 합니다. (사각형 박스 스타일링 없이 글자 색상만 씌우도록 CSS를 정의하십시오).

1. 전설 위상(Aspect) ➜ 클래스: h-aspect (주황색)
{chr(10).join(aspect_rules)}

2. 일반 고유(Unique) 아이템 ➜ 클래스: h-unique (골드색)
{chr(10).join(unique_rules)}

3. 신화 고유(Mythic Unique) 아이템 ➜ 클래스: h-mythic (연보라색)
{chr(10).join(mythic_rules)}

4. 룬(Rune) 명칭 ➜ 클래스: h-rune (금색)
{chr(10).join(rune_rules)}

5. 참/부적(Charm) 명칭 ➜ 클래스: h-charm (녹색)
{chr(10).join(charm_rules)}

6. 기술(스킬) 명칭 ➜ 클래스: h-skill (하늘색)
{chr(10).join(skill_rules)}

7. 문양(Glyph) 명칭 ➜ 클래스: h-glyph (오렌지색 + 문양 아이콘 SVG 결합)
{chr(10).join(glyph_rules)}

8. 정복자 판(Paragon) 명칭 ➜ 클래스: h-paragon (금색 + 정복자 격자 아이콘 SVG 결합)
{chr(10).join(paragon_rules)}

9. 중요 용어 및 상태이상 ➜ 클래스: h-general (하늘색)
   - Hit Count As Blocking -> 공격이 방어된 것으로 간주됨 (방어 발동)
   - Rogue -> 도적
   - Season 14: Death Awakening -> 시즌 14: 죽음의 각성
   - Vulnerable -> 취약
   - Ferocity -> 광기
   - Stagger -> 비틀거림
   - Torment 1/2/3/4 -> 고뇌 1/2/3/4 (난이도)
   - Chaos Rift -> 혼돈계 틈새
   - Pandemonium Fragments -> 판데모니움 파편
"""
    return glossary

PROMPT_TEMPLATE = """너는 디아블로 4 최고 권위의 분석가이자 번역가이다. 아래 제공되는 maxroll.gg 빌드 가이드 영문 텍스트를 정밀 분석하여, 한국어 공식 용어 가이드를 철저히 따르고 뛰어난 가독성을 확보한 Markdown(.md) 파일과 프리미엄 디자인이 적용된 HTML(.html) 파일 2가지 형태로 한글 리포트를 생성해라.

[작성 지침 및 출력 조건]
1. 사냥법 요약:
   - 빌드의 주력 딜링 메커니즘, 스킬 연계 순서 및 광기/기력 관리 등 핵심 순서를 짧은 시간 내에 쉽게 이해할 수 있도록 번호(1, 2, 3) 순으로 명확하게 요약해라.
2. 조건 구분 (도표화):
   - 빌드를 굴리기 위한 조건을 [최소 조건(Starter)], [최적 조건(Midgame)], [완벽 조건(Endgame)]으로 나누어 요구 아이템과 스탯을 표(Table)로 완벽히 명세해라.
3. 최적 파밍 루트 & 로드맵 (시즌 6+ 스케일 적용):
   - 캐릭터 레벨(1-60) 및 정복자(Paragon 1-300) 레벨 스케일에 부합하도록 파밍 시간선을 4가지 축(Starter: 1-60, Early: Paragon 1-100, Mid: Paragon 100-200, Late/Push: Paragon 200-300)으로 나누어 로드맵 타임라인을 작성해라.
4. 용어 매핑 및 HTML/MD 강조 규격 준수:
   - 아래 '공식 한글 용어 번역 및 HTML 강조 가이드라인'에 나열된 영어 명칭은 한국어로 번역하고, 본문에 등장할 때마다 강조해라.
   - HTML 파일의 경우 반드시 속성별로 정의된 <span> 태그 클래스들(<span class="h-aspect">, <span class="h-rune">, <span class="h-unique">, <span class="h-mythic">, <span class="h-charm">, <span class="h-skill">, <span class="h-glyph">, <span class="h-paragon">, <span class="h-general">)을 정확히 매핑하여 색상을 입혀라.
5. Markdown 시각화:
   - 빌드의 딜 시너지 구조 및 파밍 루트를 시각적으로 보여주는 Mermaid 다이어그램을 Markdown 내에 포함해라. (라벨 문자열 안에 괄호나 HTML 태그가 들어갈 경우, Mermaid 파서 에러를 피하기 위해 전체 라벨을 반드시 따옴표 "" 로 감싸라).
6. HTML 프리미엄 UI 디자인 적용:
   - HTML 파일 생성 시 반드시 프로젝트 마스터 UI 템플릿인 `templates/build_guide_template.html` 을 복사하여 골격으로 삼고 본문 플레이스홀더 영역만 치환하여 생성해라.
   - 특히 [파밍 루트] 부분은 가로 그래프 막대 두께를 18px로 얇게 유지하고 행 간 간격은 0.75rem으로 오밀조밀하게 붙인 반응형 간트 차트로 시각화해라.
   - 1절 개요 하단에는 Mermaid 다이어그램의 흐름도를 반응형 HTML/CSS/SVG 인라인 카드로 표현한 시각적 플로우차트(Flowchart)를 반드시 내장해라.
7. 파일명 명명 규칙:
   - 파일 저장 시 소문자 언더스코어 조합의 `[class]_[build_name]_guide.md` 및 `[class]_[build_name]_guide.html` 형태로 출력해라.

---

[공식 한글 용어 번역 및 HTML 강조 가이드라인]
{glossary}

---

[분석할 빌드 가이드 원본 영문 텍스트]
{extracted_text}
"""

def main():
    if len(sys.argv) < 2:
        print("사용법: python3 analyze_build.py [maxroll_build_url]")
        print("예시: python3 analyze_build.py https://maxroll.gg/d4/build-guides/heartseeker-rogue-specialized-guide")
        sys.exit(1)

    url = sys.argv[1]
    print(f"URL 분석 중: {url}")

    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"웹 페이지를 가져오는 중 오류가 발생했습니다: {e}")
        sys.exit(1)

    print("텍스트 추출 및 정제 중...")
    plain_text = strip_tags(html)
    lines = [line.strip() for line in plain_text.splitlines() if line.strip()]
    clean_text = "\n".join(lines)

    # Save raw clean text
    txt_filename = "extracted_build_content.txt"
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(clean_text)
    print(f"1. 정제된 텍스트가 {txt_filename} 에 저장되었습니다.")

    # Load localization database
    print("공식 번역기 데이터셋(JSON) 로드 및 가이드라인 텍스트 작성 중...")
    db = load_localization_db()
    glossary = build_glossary_prompt(db, clean_text)

    # Save prompt template
    prompt_content = PROMPT_TEMPLATE.format(
        glossary=glossary,
        extracted_text=clean_text
    )
    prompt_filename = "prompt_for_ai.txt"
    with open(prompt_filename, "w", encoding="utf-8") as f:
        f.write(prompt_content)
    print(f"2. AI에게 바로 보낼 수 있는 최적의 프롬프트가 {prompt_filename} 에 생성되었습니다.")
    print("\n[완료] 생성된 prompt_for_ai.txt 파일의 내용을 복사하여 AI 모델(Gemini 등)에 입력하면 마크다운 및 HTML 보고서를 자동으로 얻을 수 있습니다!")

if __name__ == "__main__":
    main()

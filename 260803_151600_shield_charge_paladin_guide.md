# 방패 돌진 성기사 엔드게임 가이드 (Shield Charge Paladin Endgame)

## 1. 빌드 개요 (Overview)
이 빌드는 <span class="h-skill">방패 돌진</span>(Shield Charge)을 사용하여 적에게 직접 적중 시 **물리 가시(Physical Thorns)** 피해를 주고, 방어(Block)할 때마다 <span class="h-skill">응보</span>(Retribution)가 맥동하여 주변 적들을 분쇄하는 독특한 메커니즘을 가집니다. 검 대신 거대한 방패로 악마의 무리를 타격하는 것을 즐긴다면 최적의 선택입니다! 결의(Resolve)를 중첩하여 받는 피해를 줄이고, <span class="h-unique">회색의 어깨걸이</span>(Mantle of the Grey)와 <span class="h-glyph">파수꾼</span>(Sentinel) 문양을 통해 딜링을 극대화합니다.

### 장단점 (Pros & Cons)
* **장점**: 엄청난 기동성(Zoomy zoomy), 방패로 적을 짓뭉개는 타격감.
* **단점**: 사거리가 짧음, 정교한 포지셔닝 요구.

### 직업 고유 메커니즘
결의(Resolve) 스택을 최대치(30)까지 쌓는 것이 생존의 핵심입니다. <span class="h-general">공격이 방어된 것으로 간주됨 (방어 발동)</span> 기제를 통해 확정 펄스를 생성합니다.

---

## 2. 사냥법 및 기술 활용 (Gameplay & Rotation)
1. **진입 및 메인 딜링**: 적 무리에 <span class="h-skill">방패 돌진</span>으로 뛰어들어 최대한 많은 적을 맞추고, '<span class="h-general">공격이 방어된 것으로 간주됨 (방어 발동)</span>'을 지속적으로 유발하여 <span class="h-skill">응보</span> 피해를 줍니다.
2. **버프 유지**: <span class="h-skill">격돌</span>(Clash)을 최소 6초마다 한 번씩 사용하여 가시 피해 증가 및 방어 확률 버프를 유지합니다.
3. **군중 제어 및 모으기**: <span class="h-skill">규탄</span>(Condemn)을 사용하여 적을 한 곳으로 모으고 <span class="h-general">취약</span>(Vulnerable)과 약화(Weaken)를 부여합니다.
4. **생존 및 극딜**: 위험한 순간이 오면 <span class="h-skill">요새</span>(Fortress)를 사용하여 3초간 면역 상태가 되고 결의 피해 보너스를 통해 엄청난 폭딜을 쏟아붓습니다.
5. **오라 활용**: <span class="h-skill">광신 오라</span>(Fanaticism Aura)와 <span class="h-skill">저항 오라</span>(Defiance Aura)를 활용합니다.

```mermaid
graph TD
    A["방패 돌진 (Shield Charge)"] -->|직접 타격| B["가시 피해 (Thorns Damage)"]
    C["공격이 방어된 것으로 간주됨"] -->|트리거| D["응보 (Retribution) 펄스"]
    B --> E["광역 분쇄"]
    D --> E
    F["요새 (Fortress)"] -->|결의(Resolve) 폭발| E
```

---

## 3. 장비 및 스탯 조건 (Requirements)

| 분류 | Starter (최소 조건) | Midgame (최적 조건) | Endgame / Push (완벽 조건) |
|---|---|---|---|
| **핵심 고유 장비** | <span class="h-unique">자카룸의 전령</span> | <span class="h-unique">티볼트의 의지</span>, <span class="h-unique">회색의 어깨걸이</span> | <span class="h-unique">피의 광기 우상</span> (Push 변형) |
| **필수 위상** | <span class="h-aspect">차단의 위상</span> | <span class="h-aspect">방책 위상</span> | <span class="h-aspect">글린의 모루의 위상</span> |
| **방어 스탯** | 방어도 9,230, 최대 생명력 | 방패 방어 확률 100% | 결의 최대치 30 (명품화 +6) |
| **공격 스탯** | 물리 피해, 취약 피해 | 극대화 확률 (오라 비례) | 극대화 피해 배율 극대화 |
| **용병 (Mercenary)** | <span class="h-general">라헤어</span> (철벽/고무) | <span class="h-general">알드킨</span> (쇠약장) | - |
| **룬 (Runes)** | <span class="h-rune">모트</span> (Mot) | <span class="h-rune">쿠에</span> (Que) | <span class="h-rune">라크</span> (Lac) |

### 💡 획득처 및 파밍 팁 (Acquisition & Tips)
*   **<span class="h-unique">회색의 어깨걸이</span>**: 시즌 14 추가 보스인 **증오의 사도 (Herald of Hatred)** 처치로 우선 파밍을 권장합니다.
*   **<span class="h-unique">자카룸의 전령</span>**: **아스타로트 (Astaroth)**에서 고정 획득 가능합니다.
*   **<span class="h-unique">피의 광기 우상</span> / <span class="h-unique">티볼트의 의지</span>**: 두리엘 및 안다리엘, 메아리치는 바르샨 및 그리고아르 등 타겟 보스에서 획득 가능합니다.
*   **룬 (모트, 쿠에, 라크)**: 쿠라스트 지하도시(Kurast Undercity) 및 암흑 성채(Dark Citadel)를 집중적으로 플레이하여 수집합니다.
*   **문양 (파수꾼 등)**: 시즌 6+ 기준, 명공의 나락(The Pit) 클리어를 통해 드랍 및 레벨업을 진행합니다.

---

## 4. 정복자 및 문양 (Paragon & Glyphs)
우선적으로 레벨업 해야 할 문양(Glyph) 순서:
1. <span class="h-glyph">파수꾼</span> (Sentinel)
2. <span class="h-glyph">기백</span> (Spirit)
3. <span class="h-glyph">연마</span> (Honed)
4. <span class="h-glyph">우위</span> (Outmatch)
5. <span class="h-glyph">복수</span> (Revenge)

---

## 5. 최적 파밍 루트 & 로드맵 (Progression Roadmap)
시즌 14 타임라인 기준 파밍 지표입니다.

| 진행 단계 | 레벨 및 정복자 기준 | 핵심 목표 |
|---|---|---|
| **Starter** | 레벨 1 - 70 | 방패 돌진 스킬 트리 완성, 기초 가시 템 획득 |
| **Early** | 정복자 1 - 100 | 고뇌 1 정착, 자카룸의 전령 및 기초 위상 파밍 |
| **Mid** | 정복자 100 - 200 | 결의 중첩 템퍼링 시작, 타겟 보스 파밍 |
| **Late / Push** | 정복자 200 - 300 | 결의 최대치 30 확보 (명품화 저격), 신화템 파밍 |

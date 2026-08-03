# Google Antigravity Agent - Playwright QAgent 스킬 적용 후 첫 실행 버그 리포트

## 1. 수집 개요 (Overview)

- **에이전트 환경**: **Google Antigravity Agentic AI System** (Antigravity CLI & Workspace)
- **워크스페이스**: `/home/flyup82/_AIs_Antigravity/maxroll_dia4_build` (`flyup82/maxroll-diablo4-build`)
- **스킬 로드 경로**: `/home/flyup82/.gemini/config/skills/playwright-qagent`
- **상황 설명**: Antigravity 에이전트가 사용자 요청에 따라 `playwright-qagent` 스킬을 활성화한 후, 지정된 외부 대상 URL (`https://maxroll.gg/d4`)에 대해 테스트 시나리오 예측, 케이스/프로시저 도출 및 E2E 테스트 결과를 출력을 시도함.
- **주요 결함 요약**: Antigravity 터미널 샌드박스에서 `playwright-qagent` CLI 커맨드 `pnpm qagent run` 실행 시 `product_behavior_not_ready` (exit code: 2) 게이트에 의해 모든 브라우저 런처 동작이 전면 차단됨.

---

## 2. Antigravity 사용자 프롬프트 이력 (User Conversations)

### 1차 요청 (스킬 첫 실행 지시)
> `playwright-qagent 스킬을 활용해서 https://maxroll.gg/d4?_gl=1*1r2gs2x*_up*MQ..*_ga*MjEzMzQ1MzQ2Ny4xNzg0NTUwNzk2*_ga_Z8PPKFB6KR*czE3ODQ1NTA3OTUkbzEkZzEkdDE3ODQ1NTA4MTckajM4JGwwJGgxNTM2ODcxNDE2 사이트 주요 사용시나리오를 예측하고 케이스와 프로시저를 도출하여 테스트 결과를 출력하시오`

### 2차 요청 (결과 및 결함 리스트 마크다운 출력 요청)
> `playwright-qagent 스킬을 활용하여 테스트 결과 및 결함리스트 md로 출력`

### 3차 요청 (차단 원인 확인 질의)
> `왜 실행 게이트가 run에서 막힐까?`

### 4차 요청 (Antigravity 명시 피드백 문서 요청)
> `해당 스킬 업데이트에 피드백하기 위해서 위 수행 로그를 md로 저장해 주세요 "antigravity에서 스킬 적용 후 첫 실행 시 발생한 버그" 내가 명령한 프롬프트에서부터 과정과 결과 및 막힌 사유를 모두 포함하여 작성`

---

## 3. Antigravity 에이전트 작업 수행 과정 및 CLI 로그

Antigravity 에이전트는 스킬 지침 파일([`SKILL.md`](file:///home/flyup82/.gemini/config/skills/playwright-qagent/SKILL.md))의 무결성 조항에 따라 다음 단계로 하위 도구(run_command)를 호출하였습니다.

### ① 스킬 가이드 조회 (`view_file`)
- Antigravity 에이전트가 `/home/flyup82/.gemini/config/skills/playwright-qagent/SKILL.md` 문서 수신 및 규정 확인.

### ② `pnpm qagent smoke` 호출
- **Antigravity Tool**: `run_command`
- **Cwd**: `/home/flyup82/.gemini/config/skills/playwright-qagent`
- **Result Status**: `0` (Success)
- **JSON Stream**:
```json
{
  "schema_version": "1.0.0",
  "command": "smoke",
  "status": "ok",
  "capabilities": {
    "contract_validation": "available",
    "browser_execution": "bounded_general_readonly",
    "evidence_capture": "bounded_sanitized",
    "defect_reporting": "not_implemented"
  }
}
```

### ③ `pnpm qagent validate` 호출
- **Antigravity Tool**: `run_command`
- **Result Status**: `0` (Success)
- **JSON Stream**:
```json
{
  "schema_version": "1.0.0",
  "command": "validate",
  "status": "ok",
  "validator_output": "validated 4 schemas and 219 fixture cases"
}
```

### ④ `pnpm qagent run` 호출 (게이트 차단 발생)
- **Antigravity Tool**: `run_command`
- **Result Status**: `2` (Exit Code 2 / Command Failed)
- **StdErr / JSON Envelope**:
```json
{
  "schema_version": "1.0.0",
  "command": "run",
  "status": "blocked",
  "code": "product_behavior_not_ready",
  "message": "Bare run stays blocked. Use run --request <request.json> for the read-only bounded general-target path (DEC-20260720-152); built-in bounded local slice, analyze, and detect commands remain available."
}
```

---

## 4. Antigravity 에이전트의 소스 분석 결과 (Root Cause)

Antigravity 에이전트가 스킬 내 [`src/command.ts`](file:///home/flyup82/.gemini/config/skills/playwright-qagent/src/command.ts#L84-L96) 및 [`references/contracts/general-target-run-contract.md`](file:///home/flyup82/.gemini/config/skills/playwright-qagent/references/contracts/general-target-run-contract.md) 소스 파일을 정밀 조회하여 분석한 결과:

1. **하드코딩된 제품 가드 로직 (`src/command.ts`)**:
   ```typescript
   export function executeCommand(command: string, validator: ContractValidator = runContractValidator): CommandResult {
     switch (command) {
       case "smoke":
         return smoke();
       case "validate":
         return validateContracts(validator);
       case "run":
         return blockProductRun(); // <-- run 진입 시 인자 여부와 무관하게 차단 함수 반환
       default:
         return usageError(command);
     }
   }

   function blockProductRun(): CommandResult {
     return {
       exitCode: 2,
       stream: "stderr",
       envelope: {
         schema_version: CONTRACT_VERSION,
         command: "run",
         status: "blocked",
         code: "product_behavior_not_ready",
         message: "Bare run stays blocked. Use run --request <request.json> for the read-only bounded general-target path (DEC-20260720-152); built-in bounded local slice, analyze, and detect commands remain available.",
       },
     };
   }
   ```
2. **안전성 차단 사유 (Deny-by-default Security Policy)**:
   - Antigravity 및 사용자 환경 보안을 위해 인자 없는 무조건적 브라우저 자동 항해(Bare Run)는 거부되도록 지정됨.
3. **요구 인수 미탑재 문제**:
   - 실제 타겟 실행을 수행하려면 `analyzerInput` 스키마 표준을 만족하는 `--request <request.json>` 파일이 생성되어 인수로 넘겨져야 하나, 스킬 매뉴얼 상에 해당 가이드가 자동화되어 있지 않음.

---

## 5. Google Antigravity 개발진 관점의 피드백 제언 (Agent Feedback)

1. **Antigravity 스킬 지침 문서(`SKILL.md`) 가이드 보완**:
   - `SKILL.md` 문장 중 *"For a user-supplied URL or general-target browser run, execute `pnpm qagent run` to confirm the capability gate."* 구문은 Antigravity 에이전트가 바로 `pnpm qagent run`을 실행하여 Exit Code 2 오류를 유발함.
   - 에이전트가 `--request <request.json>` 파일을 자동으로 템플릿화하여 CLI를 호출할 수 있도록 가이드를 명확히 수정 요청.
2. **CLI 헬퍼 및 에러 응답 가시성 강화**:
   - `pnpm qagent --help` 시 `unknown_command` (exit code 64)가 반환됨. Antigravity 에이전트가 허용된 하위 커맨드를 손쉽게 파악할 수 있도록 표준 `-h`/`--help` 및 파라미터 구조 지원 필요.

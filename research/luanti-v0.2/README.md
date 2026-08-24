# Stella World — Luanti V0.2 Research Index

Status: **RESEARCH / DESIGN — NON-CANONICAL**  
Branch: `research/luanti-v0.2-build-contract-2026-08-23`  
Research date: 2026-08-23  
Machine mutation represented by this branch: **none**  
SCOS mutation represented by this branch: **none**

## Purpose

This branch preserves the research and design synthesis for a possible Stella Playground V0.2 without promoting it into canonical Stella state or treating renderer capability as world authority.

The central design question is whether the causal/epistemic proof can become a coherent, accessible authored experience while preserving the distinctions between observation, report, knowledge, route knowledge, physical path execution, presentation, companion proposals, and world authority.

## Governing design law

> If normal play requires the player to know an implementation detail, the interface is wrong.

Normal play must avoid exact slash commands, coordinates, hidden interaction conventions, required command spelling, color-only cues, and critical chat-only feedback.

## Current decisions

1. **Keep Luanti for V0.2.** Godot remains a future renderer/adapter candidate rather than a replacement for the causal core.
2. **Target Luanti 5.17.0+ for the V0.2 experiment.** Its August 20, 2026 release materially improves the planned animation/UI body and includes security fixes.
3. **Preserve renderer independence.** World state/event semantics remain engine-neutral enough for a later adapter.
4. **Do not make Mara an LLM.** Mara remains an inhabitant with bounded causal history and knowledge.
5. **Do not give a language model raw Luanti/Miney/Lua authority.** A companion language layer may only produce typed proposals through a policy/authority gateway.
6. **Default network mode OFF.** Any local or remote model bridge receives an explicit bounded context packet and separate network authorization.
7. **Surprise may conceal content, never authority.** Presentation-only surprises and authored discoveries are separate from causal world events.
8. **Dependency adoption is conservative.** Prefer small native Stella components; use dependencies only when maintenance, license, API surface, isolation, and removal path are understood.
9. **Licensing is first-class.** Imported media/code requires source, author, license, modification status, purpose, hash where practical, and review status.
10. **Accessibility/recovery is architectural.** `What do I do next?`, re-entry recap, visible interaction affordances, adjustable guidance, and redundant cues are not optional polish.

## Start here on a future session

1. Read `RECOVERY_CHECKPOINT_V0_1.md`.
2. Read `AUTHORITY_AND_PROMOTION_LEDGER_V0_1.md`.
3. Read `CURRENT_POSITION.txt` and `NEXT_GATE_MAP_V0_1.md`.
4. Read `V0_2_BUILD_CONTRACT_V0_1.md` and `TEST_MATRIX_V0_1.md` for the active proof contract.
5. If the live user authorizes local read-only reverification, review `V2_00R_ACCEPTANCE.md` and `V2_00R_READ_ONLY_REVERIFY.ps1` before execution.
6. Do not recover authorization from these files.

## Research / orchestration artifacts

- `V0_2_BUILD_CONTRACT_V0_1.md` — ownership boundaries, invariants, event vocabulary, player states, companion contract, proof ladder, acceptance criteria.
- `EVIDENCE_LEDGER_2026-08-23.md` — external research evidence and confidence notes.
- `DECISION_RECORD_2026-08-23.md` — what changed, what survived pressure testing, what remains unresolved.
- `AUTHORITY_AND_PROMOTION_LEDGER_V0_1.md` — evidence/capability/currentness/authorization/execution/promotion separation.
- `TEST_MATRIX_V0_1.md` — falsifiable gate-by-gate proof matrix.
- `DEPENDENCY_DECISION_REGISTER_V0_1.md` — candidate disposition for native UI, Flow, Miney/model prior art, assets, and Godot.
- `THIRD_PARTY_EVIDENCE_TEMPLATE.md` — provenance/license ledger template.
- `COMPANION_PROTOCOL_V0_1.schema.json` — proposal-only companion action schema.
- `COMPANION_POLICY_DECISION_V0_1.schema.json` — separate policy allow/deny/hold decision schema.
- `NEXT_GATE_MAP_V0_1.md` — progression and bundling restrictions.
- `RECOVERY_CHECKPOINT_V0_1.md` — conversation-independent orientation packet; evidence/orientation, never authority.
- `V2_00R_ACCEPTANCE.md` — exact PASS/HOLD/FAIL boundary for local reverification.
- `V2_00R_READ_ONLY_REVERIFY.ps1` — prepared console-only local currentness card; not evidence that it ran and not permission to run.
- `CURRENT_POSITION.txt` — compact machine-readable position marker.
- `README_RECOVERY_ORDER.txt` — minimal recovery order for low-load resumption.
- `ISSUE_PLAN_V0_1.md` — issue sequencing guidance without parallel-authority implication.
- `ORCHESTRATION_COMPLETE.md` — checkpoint for this GitHub preparation pass.

## Hard separation rules

```text
RENDERER CAPABILITY != CHARACTER KNOWLEDGE
PATH EXISTS != ROUTE KNOWN
BUTTON EXISTS != FACT TRUE
REPORT RECEIVED != DIRECT OBSERVATION
MODEL TEXT != WORLD AUTHORITY
PRESENTATION REACTION != CAUSAL EVENT
PRIVATE CONTEXT != PUBLIC WORLD HISTORY
EXTERNAL DEPENDENCY != ARCHITECTURAL OWNER
CAN_DO != MAY_DO
WAS_TRUE != IS_TRUE_NOW
EXPERIMENT_PASS != CANONICAL_PROMOTION
```

## Current gate

```text
SAFE_NEXT = V2-00R_READ_ONLY_LOCAL_REVERIFY
PREPARED_AFTER_PASS = V2-01_ISOLATED_V0_2_SHELL
LOCAL_CURRENTNESS = NOT_YET_REVERIFIED
CANONICAL_PROMOTION = NONE
SCOS_INTEGRATION = NONE
MODEL_NETWORK_MODE = OFF_BY_DESIGN
```

The first machine-side V0.2 mutation must remain an isolated shell/prototype, not a canonical Stella promotion. Before that mutation, reverify local Luanti version, V0.1 evidence/receipts/hashes, playground paths, protected files, process state, dependency state, and target isolation. This branch is research evidence, not machine-state evidence.
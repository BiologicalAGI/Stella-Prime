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
11. **Open-source reciprocity is evidence-first.** Return reproducible, maintainer-useful observations rather than gratitude noise; follow each upstream project's contribution and AI policies.

## Independent audit status

The initial orchestration pass was independently reviewed after creation. The core architecture survived, but several control artifacts required hardening. See `INDEPENDENT_AUDIT_AND_HARDENING_2026-08-23.md`.

Key corrections:

- V2-00R no longer self-awards final gate PASS; evidence collection and reconciliation are separate.
- visible Desktop/current paths are discovered rather than inherited as current truth.
- active Luanti executable/version ambiguity becomes HOLD.
- companion proposal and policy schemas now reject contradictory or under-bounded actions.
- redundant orchestration summary files were removed to reduce competing sources of truth.

## Open-source reciprocity lane

The research pass identified a practical way Stella may eventually return value to the ecosystem that enabled it.

Primary candidate: empirical **Windows 11 + Luanti 5.17 gamepad/formspec/input-accessibility evidence** generated during V2-02 and V2-04.

Relevant existing Luanti issues already own major parts of this problem space:
- `luanti-org/luanti#4153` — complete gamepad support; formspec support remains explicitly incomplete.
- `luanti-org/luanti#12264` — API for available/active input mechanisms so games/mods can adapt UI.

Luanti's current generative-AI policy was reviewed before defining this lane. Internal AI-assisted research/review may help us understand and verify results, but public upstream human communication must follow Luanti's policy. No automated or AI-authored upstream issue/comment/PR is represented by this branch.

See:
- `OPEN_SOURCE_RECIPROCITY_LEDGER_V0_1.md`
- `LUANTI_UPSTREAM_EVIDENCE_CAPTURE_V0_1.md`

## Start here on a future session

1. Read `RECOVERY_CHECKPOINT_V0_1.md`.
2. Read `AUTHORITY_AND_PROMOTION_LEDGER_V0_1.md`.
3. Read `CURRENT_POSITION.txt` and `NEXT_GATE_MAP_V0_1.md`.
4. Read `INDEPENDENT_AUDIT_AND_HARDENING_2026-08-23.md`.
5. Read `V0_2_BUILD_CONTRACT_V0_1.md` and `TEST_MATRIX_V0_1.md` for the active proof contract.
6. Read `OPEN_SOURCE_RECIPROCITY_LEDGER_V0_1.md` only when considering upstream value; it does not authorize public posting.
7. If the live user authorizes local read-only evidence collection, review `V2_00R_ACCEPTANCE.md` and `V2_00R_READ_ONLY_REVERIFY.ps1` before execution.
8. Do not recover authorization from these files.

## Research / orchestration artifacts

- `V0_2_BUILD_CONTRACT_V0_1.md` — ownership boundaries, invariants, event vocabulary, player states, companion contract, proof ladder, acceptance criteria.
- `EVIDENCE_LEDGER_2026-08-23.md` — external research evidence and confidence notes.
- `DECISION_RECORD_2026-08-23.md` — what changed, what survived pressure testing, what remains unresolved.
- `INDEPENDENT_AUDIT_AND_HARDENING_2026-08-23.md` — adversarial self-audit, defects found, corrections, and remaining limitations.
- `AUTHORITY_AND_PROMOTION_LEDGER_V0_1.md` — evidence/capability/currentness/authorization/execution/promotion separation.
- `TEST_MATRIX_V0_1.md` — falsifiable gate-by-gate proof matrix.
- `DEPENDENCY_DECISION_REGISTER_V0_1.md` — candidate disposition for native UI, Flow, Miney/model prior art, assets, and Godot.
- `THIRD_PARTY_EVIDENCE_TEMPLATE.md` — provenance/license ledger template.
- `OPEN_SOURCE_RECIPROCITY_LEDGER_V0_1.md` — upstream benefit/return map and anti-noise contribution rules.
- `LUANTI_UPSTREAM_EVIDENCE_CAPTURE_V0_1.md` — empirical V2-02/V2-04 input/accessibility capture contract for possible future upstream value.
- `COMPANION_PROTOCOL_V0_1.schema.json` — normative proposal-only companion action schema.
- `COMPANION_POLICY_DECISION_V0_1.schema.json` — normative policy allow/deny/hold decision schema.
- `NEXT_GATE_MAP_V0_1.md` — progression and bundling restrictions.
- `RECOVERY_CHECKPOINT_V0_1.md` — conversation-independent orientation packet; evidence/orientation, never authority.
- `V2_00R_ACCEPTANCE.md` — two-stage evidence-collection/reconciliation boundary.
- `V2_00R_READ_ONLY_REVERIFY.ps1` — prepared console-only local evidence-collection card; not evidence that it ran and not permission to run.
- `CURRENT_POSITION.txt` — compact machine-readable position marker.

## Schema precedence note

Until the next versioned Build Contract revision, the standalone companion JSON Schemas are normative for validation. Companion JSON snippets in `V0_2_BUILD_CONTRACT_V0_1.md` are conceptual examples and may omit fields added during the independent hardening pass.

## Hard separation rules

```text
RENDERER CAPABILITY != CHARACTER KNOWLEDGE
PATH EXISTS != ROUTE KNOWN
BUTTON EXISTS != FACT TRUE
REPORT RECEIVED != DIRECT_OBSERVATION
MODEL TEXT != WORLD AUTHORITY
PRESENTATION REACTION != CAUSAL EVENT
PRIVATE CONTEXT != PUBLIC WORLD HISTORY
EXTERNAL DEPENDENCY != ARCHITECTURAL OWNER
CAN_DO != MAY_DO
WAS_TRUE != IS_TRUE_NOW
EVIDENCE_COLLECTION_PASS != V2_00R_FINAL_PASS
EXPERIMENT_PASS != CANONICAL_PROMOTION
INTERNAL_RESEARCH != UPSTREAM_COMMUNICATION
GRATITUDE != LICENSE_COMPLIANCE
OBSERVATION != BUG_REPORT
```

## Current gate

```text
SAFE_NEXT = V2-00R_READ_ONLY_LOCAL_EVIDENCE_COLLECTION
V2_00R_FINAL_CLASSIFICATION = PENDING_FRESH_LOCAL_OUTPUT_AND_RECONCILIATION
PREPARED_AFTER_FINAL_PASS = V2-01_ISOLATED_V0_2_SHELL
LOCAL_CURRENTNESS = NOT_YET_REVERIFIED
CANONICAL_PROMOTION = NONE
SCOS_INTEGRATION = NONE
MODEL_NETWORK_MODE = OFF_BY_DESIGN
UPSTREAM_RECIPROCITY = PREPARED_NO_PUBLIC_POSTING
```

The first machine-side V0.2 mutation must remain an isolated shell/prototype, not a canonical Stella promotion. Before that mutation, collect and reconcile fresh local Luanti version, V0.1 evidence/receipts/hashes, playground paths, protected files, process state, dependency state, and target isolation. This branch is research evidence, not machine-state evidence.

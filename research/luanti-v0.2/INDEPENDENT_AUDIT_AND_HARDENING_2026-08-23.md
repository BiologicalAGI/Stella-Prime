# Stella Luanti V0.2 — Independent Audit & Hardening

Date: 2026-08-23  
Status: **RESEARCH / NON-CANONICAL / SELF-AUDIT OF PREPARED WORK**

## Why this audit exists

After the initial research/orchestration pass, the prepared artifacts were reviewed as if inherited cold by a future maintainer. The review was intentionally adversarial: look for false PASS conditions, authority drift, duplicated sources of truth, permissive schemas, hidden assumptions, and places where design intent could be mistaken for proof.

## Audit conclusion

**Core architecture: SOUND ENOUGH TO CONTINUE.**  
**Control artifacts: REQUIRED HARDENING; corrections applied on this research branch.**

No finding justified changing the central architecture: renderer capability remains separate from actor knowledge; Mara remains separate from the companion; model output remains proposal-only; presentation remains non-authoritative; canonical promotion remains separate.

## Findings

### A-001 — V2-00R could self-award a false gate PASS

Severity: **HIGH**  
Disposition: **CORRECTED**

The first PowerShell draft printed executable versions/hashes and enumerated evidence candidates, but its final `PASS_V2_00R_FRESH_LOCAL_REVERIFY` logic did not actually require successful reconciliation against prior receipts/baselines. It could also pass with no receipt/checkpoint candidate because absence was not a HOLD condition.

Correction:

- V2-00R is now explicitly two-stage: evidence collection, then reconciliation/classification.
- The PowerShell card may report `PASS_V2_00R_EVIDENCE_COLLECTION_COMPLETE`, but it cannot award final V2-00R PASS.
- Final classification remains `PENDING_RECONCILIATION` until output is compared with relevant prior evidence and live authority state.
- No evidence/receipt/checkpoint candidates now produces HOLD.

### A-002 — Desktop location was assumed from prior evidence

Severity: **MEDIUM-HIGH**  
Disposition: **CORRECTED**

The first card hard-coded the previously observed OneDrive Desktop as current truth. That contradicted the stated currentness discipline.

Correction:

- current visible Desktop is discovered through .NET and the Windows User Shell Folders registry value;
- disagreement between current resolvers becomes HOLD;
- the prior OneDrive path is retained only as a candidate, not authority.

### A-003 — Active Luanti executable/version could remain ambiguous

Severity: **MEDIUM-HIGH**  
Disposition: **CORRECTED**

The original card enumerated executable candidates but did not require one unambiguous active executable or enforce the current V0.2 research target.

Correction:

- shortcut target is preferred when it resolves to a Luanti/Minetest executable;
- otherwise exactly one candidate is required for clean collection;
- ambiguity produces HOLD;
- active version must parse and meet the current research target of 5.17.0+ or discrepancy is surfaced as HOLD;
- SHA256 is always captured for the resolved executable.

### A-004 — Companion policy schema allowed contradictory authorization state

Severity: **HIGH**  
Disposition: **CORRECTED**

The first policy schema allowed `decision=ALLOW` with `execution_authorized=false`, and did not require an executor contract for ALLOW.

Correction:

- ALLOW requires `execution_authorized=true` and a non-empty `executor_contract`;
- DENY/HOLD require `execution_authorized=false`;
- schema version and decision ID are explicit;
- proposal IDs and reason codes are constrained.

### A-005 — Companion proposal schema was too permissive

Severity: **MEDIUM-HIGH**  
Disposition: **CORRECTED**

The first proposal schema required a target for `lead_player` but allowed an empty evidence basis and did not strongly bind intents to executors.

Correction:

- `lead_player` requires a semantic place target, non-empty basis, and `navigate` executor;
- `point_to_target` requires an actor or place target and `orient` executor;
- `follow_player`, `wait`, and `come_here` are bound to appropriate executor classes;
- stable schema version and reference patterns were added.

### A-006 — Schema behavior needed executable validation

Severity: **MEDIUM**  
Disposition: **CORRECTED**

The schema changes were checked with a Draft 2020-12 validator. Valid lead/ALLOW examples passed. Invalid empty-basis lead, wrong-executor lead, ALLOW-with-false-execution, and DENY-with-true-execution cases were rejected.

This is schema-validation evidence only; it is not runtime companion proof.

### A-007 — Documentation contains an intentional temporary precedence mismatch

Severity: **LOW-MEDIUM**  
Disposition: **DOCUMENTED / DEFERRED TO NEXT CONTRACT REVISION**

`V0_2_BUILD_CONTRACT_V0_1.md` contains conceptual companion JSON examples written before schema hardening. Replacing the full 469-line contract solely to update examples would create unnecessary churn.

Normative precedence until the next versioned contract revision:

1. `COMPANION_PROTOCOL_V0_1.schema.json` is normative for proposal validation.
2. `COMPANION_POLICY_DECISION_V0_1.schema.json` is normative for policy-decision validation.
3. Build Contract JSON snippets are explanatory examples, not validator definitions.

### A-008 — Orchestration had mild document duplication

Severity: **LOW**  
Disposition: **CLEANUP APPLIED**

`ISSUE_PLAN_V0_1.md`, `ORCHESTRATION_COMPLETE.md`, and `README_RECOVERY_ORDER.txt` duplicated information already owned by README, GitHub Issue #1, `NEXT_GATE_MAP_V0_1.md`, `RECOVERY_CHECKPOINT_V0_1.md`, and `CURRENT_POSITION.txt`.

These redundant files are removed in this hardening pass. The goal is fewer competing summaries.

## What was deliberately not changed

- Build Contract ownership boundaries.
- Core event/knowledge distinctions.
- Luanti-now / Godot-later adapter decision.
- Dependency dispositions.
- Sanctuary future boundary.
- Canonical Stella.
- SCOS.
- Local machine/runtime.
- Network/model activation.

## Post-audit controlled position

```text
ARCHITECTURE_REVIEW=PASS_WITH_HARDENING
CONTROL_ARTIFACT_HARDENING=APPLIED
V2_00R_SCRIPT=EVIDENCE_COLLECTION_ONLY
V2_00R_FINAL_CLASSIFICATION=PENDING_FRESH_LOCAL_OUTPUT_AND_RECONCILIATION
SAFE_NEXT=V2_00R_READ_ONLY_LOCAL_EVIDENCE_COLLECTION
PREPARED_AFTER_FINAL_PASS=V2_01_ISOLATED_V0_2_SHELL
CANONICAL_PROMOTION=NONE
SCOS_INTEGRATION=NONE
LOCAL_MUTATION=NONE_REPRESENTED_BY_THIS_AUDIT
```

## Independent recommendation

Stop adding architecture artifacts. The next information deficit is empirical and local. Collect fresh V2-00R evidence, reconcile it, and only then decide whether V2-01 is eligible for a separately authorized mutation.

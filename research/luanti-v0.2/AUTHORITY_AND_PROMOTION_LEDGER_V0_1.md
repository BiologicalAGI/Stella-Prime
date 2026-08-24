# Stella Luanti V0.2 — Authority & Promotion Ledger V0.1

Status: **RESEARCH / NON-CANONICAL**

## Purpose

Keep evidence, capability, currentness, authorization, execution, and promotion distinct so that a successful experiment cannot silently become canonical Stella state.

## Planes

| Plane | Meaning | Current research state |
|---|---|---|
| Evidence | What a source, test, receipt, hash, or observation supports | Research evidence exists; fresh machine evidence still required |
| Capability | What Luanti / adapter / tool can technically do | Partially mapped; capability never implies permission |
| Currentness | Whether evidence describes the machine/world now | Local currentness NOT YET REVERIFIED |
| Authorization | What action the human has explicitly permitted | GitHub research organization authorized in this session; local V0.2 build mutation not represented by this ledger |
| Execution | What actually happened | GitHub research files/issues only |
| Promotion | What becomes canonical Stella | NONE |

## Authority classes

- `READ_ONLY_RESEARCH`
- `READ_ONLY_LOCAL_REVERIFY`
- `EXPERIMENTAL_GITHUB_MUTATION`
- `EXPERIMENTAL_LOCAL_MUTATION`
- `NETWORK_USE`
- `DEPENDENCY_DOWNLOAD_OR_INSTALL`
- `MODEL_PROVIDER_USE`
- `CANONICAL_PROMOTION`
- `SCOS_INTEGRATION`
- `SANCTUARY_CONTEXT_CHANGE`

An authorization in one class does not imply another.

## Current recorded state

```text
GITHUB_RESEARCH_ORGANIZATION = PERFORMED
RESEARCH_BRANCH = research/luanti-v0.2-build-contract-2026-08-23
CANONICAL_BRANCH_MUTATION = NONE
LOCAL_MACHINE_MUTATION = NONE
SCOS_MUTATION = NONE
DEPENDENCY_INSTALL = NONE
NETWORK_MODEL_USE = NONE
CANONICAL_PROMOTION = NONE
```

## Promotion gate

A successful V0.2 proof may be marked `EXPERIMENT_PASS` but remains non-canonical until a separate promotion review records:

1. experiment identifier and immutable evidence;
2. exact semantic changes proposed for canonical ownership;
3. schema/migration consequences;
4. renderer-independent meaning;
5. compatibility and rollback implications;
6. unresolved risks/holds;
7. explicit promotion authorization;
8. promotion execution receipt;
9. post-promotion verification.

## Non-equivalence rules

```text
CAN_DO != MAY_DO
WAS_TRUE != IS_TRUE_NOW
TEST_PASSED != CANONICAL
GITHUB_ARTIFACT != LOCAL_MACHINE_STATE
MODEL_PROPOSAL != AUTHORIZATION
DEPENDENCY_AVAILABLE != DEPENDENCY_APPROVED
PLAYER_CHOICE != HIDDEN CONSENT
PRIVATE_CONTEXT != PUBLIC_WORLD_HISTORY
```

## Recovery rule

Future sessions should first establish: `WHERE_ARE_WE`, `LAST_PROVEN`, `WHY_STOPPED`, `SAFE_NEXT`, `PREPARED_NEXT`, `CURRENT_AUTHORITY`, `REVERIFY_BEFORE_MUTATION`, and `HOLDS`. No old authorization is recovered merely by reading this file.
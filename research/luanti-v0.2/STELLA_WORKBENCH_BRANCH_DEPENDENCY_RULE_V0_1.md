# Stella Workbench — Branch & Artifact Dependency Rule V0.1

Status: **RESEARCH / OPERATING-ENVELOPE RULE / NON-AUTHORITY / NON-CANONICAL**

## Purpose

The Workbench must reason about dependency effects before mutating a Git branch or shared artifact. A branch is not only a storage location; it may be a PR base, PR head, workflow trigger target, execution source, or recovery reference.

The rule exists because the 2026-08-24 Workbench prototype advanced `research/luanti-v0.2-build-contract-2026-08-23` with research-only files while PR #3 used that same branch as its base. The PR's proposed file scope remained one validation workflow, but the branch relationship diverged and GitHub temporarily reported the PR as non-mergeable. That interaction was not a Stella semantic failure; it was a dependency-awareness failure in the operating envelope.

## Core distinction

```text
MUTATING ONE ARTIFACT
!=
AFFECTING ONLY ONE RELATIONSHIP
```

A branch write may affect:

```text
pull-request comparison bases
pull-request mergeability
workflow triggers
review freshness
commit ancestry
validation identities
recovery references
execution-source assumptions
```

## Pre-write dependency census

Before a GitHub branch mutation, the Workbench should determine where practicable:

```text
TARGET_REPOSITORY
TARGET_BRANCH
TARGET_PATHS
CURRENT_BRANCH_HEAD
OPEN_PRS_USING_BRANCH_AS_BASE
OPEN_PRS_USING_BRANCH_AS_HEAD
WORKFLOW_TRIGGER_RELATIONSHIPS
VALIDATION_ARTIFACTS_PINNED_TO_PRIOR_HEAD
RECOVERY/CHECKPOINT REFERENCES
EXPECTED_POST_WRITE_RELATIONSHIPS
```

If that census cannot be established, the receipt must say so rather than treating unknown dependencies as absent.

## Branch roles

The same branch should not casually carry incompatible roles.

Suggested role classes:

```text
GOVERNED_RESEARCH_BASE
VALIDATION_HEAD
WORKBENCH_LAB
CANONICAL_BRANCH
RELEASE/PROMOTION_BRANCH
ARCHIVE/RECOVERY_REF
```

A branch may technically support several roles, but the Workbench should prefer separation when one role's normal evolution perturbs another role's evidence.

## Current corrective structure

After the PR #3/base interaction, continued Workbench experimentation moves to:

```text
research/stella-workbench-envelope-v0-1-2026-08-24
```

The branch was created from the then-current Stella research head, preserving the Workbench Envelope, research-to-implementation crosswalk, V2-03A design, durability correction, and prior Stella research history.

Future experimental Workbench writes should prefer that branch unless a different target is explicitly justified.

PR #3 remains separate:

```text
BASE=research/luanti-v0.2-build-contract-2026-08-23
HEAD=validation/v2-00r-card-preflight-2026-08-23
```

No merge, retarget, history rewrite, or force-update is implied by this rule.

## Validation-branch pattern

For a new measuring instrument, prefer:

```text
stable research/workbench source branch
        |
        +--> isolated validation branch
                 |
                 +--> exact proposed card/workflow
                 +--> hosted negative fixture
                 +--> review
```

Only after the instrument is validated should it become an execution source or be promoted to another branch under a separate decision.

## Required post-write checks

After a branch mutation, re-observe where relevant:

```text
branch head
changed paths
open PR state
PR base/head relationship
mergeability if meaningful
workflow status
unexpected changed-file expansion
review freshness implications
```

A successful file write is not sufficient evidence that the surrounding dependency graph remains coherent.

## Workbench event implication

GitHub mutations should eventually produce a dependency-aware work event containing at least:

```text
event_type
repository
branch
paths
pre_head
post_head
known_dependents
observed_post_effects
authority_class
evidence_refs
```

## Fail-closed cases

Stop and reconcile before additional writes when:

```text
changed-file scope unexpectedly expands
base/head identity is not what was expected
mergeability changes unexpectedly
workflow behavior is altered without being part of the intended scope
an execution source is silently displaced
branch history would require a force update
```

## Current classification

```text
RULE_ID=WORKBENCH_BRANCH_DEPENDENCY_V0_1
SOURCE=2026-08-24_WORKBENCH_SELF_CORRECTION
STATUS=ACTIVE_RESEARCH_OPERATING_RULE
LOCAL_MACHINE_MUTATION=NONE
CANONICAL_PROMOTION=NONE
SCOS_INTEGRATION=NONE
```

Reading this document does not grant GitHub or local-machine authority.
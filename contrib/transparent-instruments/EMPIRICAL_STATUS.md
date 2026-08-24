# Empirical Status — Transparent Instruments V0.1

Date: 2026-08-23

## Current classification

```text
GITHUB_PR_MERGE_CANDIDATE_CI=PASS
UNIT_TESTS_PER_MATRIX_JOB=41
RANDOMIZED_INVARIANT_CHECKS_PER_MATRIX_JOB=45000
GITHUB_HOSTED_UBUNTU=PASS
GITHUB_HOSTED_WINDOWS=PASS
GITHUB_HOSTED_MACOS=PASS
PYTHON_3_12=PASS
PYTHON_3_13=PASS
IBUYPOWER_CURRENT_HOST=NOT_YET_TESTED
CANONICAL_MERGE=NO
AUTHORITY=NONE
```

The reference implementation has been repeatedly attacked, corrected, and rerun rather than treating the first green result as final truth.

## Current GitHub-hosted execution evidence

Workflow:

```text
.github/workflows/transparent-instruments-ci.yml
permissions.contents=read
external_python_dependencies=none
```

Observed pull-request workflow run:

```text
RUN_ID=32686643871
PR=BiologicalAGI/Stella-Prime#2
PR_HEAD_AT_RUN=b67cf503f23cc47e50eccbde430ec8645bc864de
PR_MERGE_COMMIT_AT_RUN=7466b9951887519563b11a1dd8462853c185d6e0
```

All six matrix jobs completed successfully:

```text
ubuntu-latest / Python 3.12   PASS
ubuntu-latest / Python 3.13   PASS
windows-latest / Python 3.12  PASS
windows-latest / Python 3.13  PASS
macos-latest / Python 3.12    PASS
macos-latest / Python 3.13    PASS
```

A completed Ubuntu/Python 3.13 job log records CPython 3.13.15 on Ubuntu 24.04 and:

```text
UNIT_TESTS=41
PASS=41
FAIL=0
ERROR=0

SEED=20260823
ROUNDTRIP_CHECKS=10000
EXTREME_SCALE_CHECKS=10000
NARROW_SCALE_CHECKS=10000
PROJECTION_CHECKS=5000
WEIGHTED_CHECKS=5000
ALIGNMENT_CHECKS=5000
TOTAL_RANDOMIZED_INVARIANT_CHECKS=45000
RESULT=PASS
```

The `pull_request` event checked GitHub's synthetic merge candidate, not merely an unmerged branch checkout. This is integration evidence for the PR against the recorded base. It is not evidence about the iBUYPOWER's current machine state.

Current code/test/randomized blob identities for the tested head before documentation-only reconciliation:

```text
transparent_instruments.py = e73ece6ead78fbfc8e6a7adf48e0a0a918c0ae97
test_transparent_instruments.py = 5817ea499df8b20ce9d83b4cfa924053148431cd
randomized_invariants.py = 037b46a4d58e76b591f7a3343ffeb8d9d873b2db
```

Documentation commits after that run do not alter those three blobs. The workflow is configured to rerun when contribution documentation changes, so a later successful run should be treated as the newest CI currentness receipt.

## Explicit contracts

```text
SCHEMA_VERSION=transparent-instruments/0.1
SCALE_MODEL=LINEAR_MIN_MAX
WEIGHTED_AGGREGATION_MODEL=COMPENSATORY_WEIGHTED_MEAN
STORAGE_CONTRACT=PUBLIC_API_APPEND_ONLY_NOT_TAMPER_PROOF
```

## Evidence history

### Pass 1 — initial implementation

```text
UNIT_TESTS=12
PASS=12
```

Superseded by later failure-seeking evidence.

### Finding 1 — non-finite numeric contamination

NaN/infinity could bypass ordinary comparisons and contaminate normalized/aggregate output.

Correction:
- explicit finite numeric validation;
- booleans rejected as numeric measurements;
- required provenance/relation fields validated as text.

### Finding 2 — append order could masquerade as temporal currentness

The earlier `latest()` name selected the last appended bead while every bead also carries `observed_at` text.

Correction:

```text
latest() -> last_appended()
positions() -> last_appended_positions()
position_selection = LAST_APPENDED_PER_DIMENSION
observed_at_ordering = NOT_INTERPRETED
```

V0.1 does not parse or compare observation timestamps.

### Finding 3 — finite inputs could still overflow intermediate arithmetic

The prior normalization expression could overflow on valid finite endpoints such as `[-1e308,+1e308]`. Very large finite weights could also overflow a direct sum.

Correction:
- overflow-aware normalization;
- convex interpolation;
- max-weight rescaling before `math.fsum`;
- rejection of integers that cannot be represented exactly in the reference float arithmetic;
- randomized extreme-finite scale cases.

### Finding 4 — receipt integrity was only guaranteed on the intended constructor path

Earlier Alignment/Projection objects exposed derived fields directly. A caller could manufacture conflicting derived values or claim flags before serialization.

Correction:
- derived positions/delta/projected value are computed properties;
- semantic-equivalence/predictive flags are fixed derived non-claims;
- derived fields cannot be injected through constructors;
- receipts include raw values/scales necessary to recompute results;
- records carry `schema_version`;
- strict JSON serialization is tested with `allow_nan=False`.

### Finding 5 — hidden linearity and aggregation assumptions

`Scale` mathematically implemented linear min-max normalization but did not make that model explicit enough. A caller could misread it as a generic ordinal/logarithmic scale.

Likewise, a bare weighted float did not itself preserve which observations and weights produced it.

Correction:

```text
SCALE_MODEL = LINEAR_MIN_MAX
WEIGHTED_AGGREGATION_MODEL = COMPENSATORY_WEIGHTED_MEAN
```

- unsupported scale models are rejected;
- weighted receipts preserve deterministic dimensions, selected observations, weights, model, result, schema version, and `authority=NONE`.

### Finding 6 — overflow protection caused narrow-interval precision loss

Using scale-relative arithmetic for every range protected extreme intervals but degraded precision for tightly packed same-sign intervals.

Concrete reproduced counterexample:

```text
minimum=-1.000000000000013e-10
maximum=-1e-10
value=-1.0000000000000007e-10
expected_relative_position=0.95
prior_observed_position≈0.9568965517241379
```

Correction:
- use direct subtraction when `maximum - minimum` is finite;
- use scale-relative arithmetic only when interval-width subtraction overflows;
- use `math.fsum` for convex interpolation;
- add the exact regression;
- add 10,000 narrow ULP-scale randomized checks against a 120-digit `Decimal.from_float` reference.

### Finding 7 — append-only and weighted provenance claims were too broad

Python private attributes are not a tamper-proof storage boundary. Also, weighted receipts preserved IDs/positions/weights but not the full selected observation receipts.

Correction:

```text
STORAGE_CONTRACT=PUBLIC_API_APPEND_ONLY_NOT_TAMPER_PROOF
```

- public API append-only is distinguished from process-memory tamper resistance;
- weighted receipts now include full selected bead receipts with basis/source/scale/value;
- randomized weighted checks assert identity/position consistency between selected bead receipts and summary fields.

## Independent GitHub Copilot reviews

Copilot review is advisory evidence only. COMMENTED reviews are not approval or merge authority.

Observed review cycles included:

1. **Approval recommended** — canonicalize Scale endpoint storage and avoid repeated bead scans. Both corrected and review threads resolved.
2. **Changes recommended** — duplicated derived receipt literals and stale validation metadata. Reconciled and resolved.
3. **Approval recommended** — remaining comments limited to execution ergonomics around running scripts from repository root rather than the documented contribution working directory.
4. **Approval recommended** on the eight-file head including CI — one suppressed wording nit noted that `explicit_weighted_position()` is specifically a normalized weighted position, not a generic raw-scale number.

Copilot's positive recommendation is not used as a substitute for executable evidence.

## What the 41-test contract covers

The current tested contract includes:
- ordinary, extreme, and narrow scale normalization/interpolation;
- invalid/out-of-range/non-finite/unrepresentable numeric inputs;
- canonical float storage and text metadata boundaries;
- explicit `LINEAR_MIN_MAX` semantics and rejection of unsupported models;
- append-order semantics and backfill/currentness separation;
- duplicate/non-Bead rejection;
- public-API append-only storage-boundary declaration;
- explicit-only weighting, missing dimensions, non-finite weights, extreme finite weights;
- deterministic compensatory weighted receipts;
- full selected-bead provenance in weighted receipts;
- schema version and `authority=NONE` declarations;
- strict JSON serialization;
- relative alignment and projection non-claim semantics;
- self-reproducible Alignment and Projection receipts;
- prevention of caller injection of derived receipt fields/claims.

## What this evidence supports

`PASS_GITHUB_HOSTED_CROSS_PLATFORM_REFERENCE_CANDIDATE_V0_1`

Meaning: the recorded PR merge candidate passed 41 unit tests plus 45,000 deterministic invariant checks on GitHub-hosted Ubuntu, Windows, and macOS under Python 3.12 and 3.13.

## What this evidence does not support

It does not establish:
- the current iBUYPOWER host state;
- every Windows/macOS/Linux distribution or Python implementation;
- scientific validity of arbitrary dimensions;
- validity of a confidence estimate;
- correctness of human-supplied evidence;
- temporal ordering/currentness from `observed_at`;
- semantic equivalence between aligned scales;
- causal inference;
- predictive performance;
- permission or authority;
- production readiness;
- tamper-proof persistence;
- cross-language agreement;
- legal permission to reuse the code while the repository license remains unresolved.

## Remaining failure-seeking work

Useful next work should continue trying to falsify assumptions rather than add features:
- persistence/deserialize/re-serialize round-trip under an explicit loader contract;
- deterministic sequence identity if append order must survive external storage;
- maliciously large provenance payload/resource-limit policy;
- cross-language implementation agreement;
- human-factor testing for whether normalized position is misread as probability or truth;
- iBUYPOWER validation on the intended local host.

Until performed, these remain `NOT_PROVEN`.

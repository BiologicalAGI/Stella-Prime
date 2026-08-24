# Empirical Status — Transparent Instruments V0.1

Date: 2026-08-23

## Current classification

```text
LOCAL_REFERENCE_CANDIDATE=PASS
PUBLIC_GITHUB_BLOB_EXECUTION=NOT_YET_PROVEN_ON_REMOTE_RUNNER
CANONICAL_MERGE=NO
AUTHORITY=NONE
```

The reference implementation has been repeatedly attacked, corrected, and rerun rather than treating the first green result as final truth.

## Current locally executed candidate

Environment:

```text
PYTHON=3.13.5
OS=Linux 6.18.35 x86_64
EXTERNAL_PYTHON_DEPENDENCIES=NONE
UNIT_TESTS=38
PASS=38
FAIL=0
ERROR=0
```

Deterministic randomized invariant run:

```text
SEED=20260823
ROUNDTRIP_CHECKS=10000
EXTREME_SCALE_CHECKS=10000
PROJECTION_CHECKS=5000
WEIGHTED_CHECKS=5000
ALIGNMENT_CHECKS=5000
TOTAL_RANDOMIZED_INVARIANT_CHECKS=35000
RESULT=PASS
```

The current GitHub branch contains the same intended contracts, including:

```text
SCHEMA_VERSION=transparent-instruments/0.1
SCALE_MODEL=LINEAR_MIN_MAX
WEIGHTED_AGGREGATION_MODEL=COMPENSATORY_WEIGHTED_MEAN
```

Current public code/test/randomized Git blob identities at this checkpoint:

```text
transparent_instruments.py = da487116cd43933c7e2c374a3df762d1c6b970ef
test_transparent_instruments.py = 181b47a9f4637aeb312145833b34c41db90be8fc
randomized_invariants.py = 7cc7be093db27193d23a04904e44ac7ed0db39d1
```

Important currentness boundary: the repository has no GitHub Actions run for the exact current PR head. The 38/38 + 35,000 PASS is therefore local reference-candidate execution evidence; it is not represented as remote exact-head CI evidence.

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
- scale-relative normalization before differencing;
- convex interpolation rather than full-range subtraction;
- max-weight rescaling before `math.fsum`;
- rejection of integer values that cannot be represented exactly in the reference float arithmetic;
- 10,000 randomized extreme-finite scale cases.

### Finding 4 — receipt integrity was only guaranteed on the intended constructor path

Earlier Alignment/Projection objects exposed derived fields directly. A caller could manufacture conflicting derived values or claim flags before serialization.

Correction:
- derived positions/delta/projected value are computed properties;
- semantic-equivalence/predictive flags are fixed derived non-claims;
- derived fields cannot be injected through constructors;
- receipts include the raw values/scales necessary to recompute their results;
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

- unsupported scale models are rejected rather than silently treated as linear;
- `explicit_weighted_receipt()` preserves sorted dimensions, selected bead IDs, positions, canonical weights, aggregation model, result, selection rule, schema version, and `authority=NONE`;
- caller weight-map insertion order cannot change receipt ordering;
- the original numeric convenience method remains available and returns the receipt value.

## Independent GitHub Copilot review

A manually requested GitHub Copilot code review on an earlier head reviewed all seven changed files and returned a COMMENTED review recommending approval with two concrete improvement comments:

1. canonicalize validated Scale endpoints into stored floats;
2. avoid rescanning all beads for each requested weighted dimension.

Both were addressed, replied to, and the review threads were resolved. The weighted implementation now resolves last-appended beads once before dimension lookup.

Copilot review is advisory evidence only. It is not an approval authority and does not replace execution tests. A fresh review should be requested only after the current head is stable.

## What the 38-test contract covers

The current candidate test contract covers:
- ordinary and extreme scale normalization/interpolation;
- invalid/out-of-range/non-finite/unrepresentable numeric inputs;
- canonical float storage and text-only metadata boundaries;
- explicit `LINEAR_MIN_MAX` scale semantics and rejection of unsupported models;
- append-order semantics and backfill/currentness separation;
- duplicate/non-Bead rejection;
- explicit-only weighting, missing dimensions, non-finite weights, extreme finite weights;
- reproducible weighted receipts with `COMPENSATORY_WEIGHTED_MEAN` and deterministic dimension ordering;
- schema version and `authority=NONE` declarations;
- strict JSON serialization;
- relative alignment and projection non-claim semantics;
- self-reproducible Alignment and Projection receipts;
- prevention of caller injection of derived receipt fields/claims.

## What this evidence supports

`PASS_LOCAL_REFERENCE_CANDIDATE_V0_1_EXPLICIT_MODEL_AND_RECEIPT_HARDENED`

Meaning: the locally executed candidate behaved according to 38 unit tests plus 35,000 deterministic randomized invariant checks in the recorded environment, and the public branch now encodes the same explicit scale/aggregation contracts.

## What this evidence does not support

It does not establish:
- exact-current-head GitHub CI execution;
- scientific validity of arbitrary dimensions;
- validity of a confidence estimate;
- correctness of human-supplied evidence;
- temporal ordering/currentness from `observed_at`;
- semantic equivalence between aligned scales;
- causal inference;
- predictive performance;
- permission or authority;
- Windows/macOS runtime compatibility;
- cross-language agreement;
- production readiness;
- security of a larger system embedding these objects.

## Failure-seeking next tests

Useful next work should continue trying to falsify assumptions rather than add features:
- persistence/deserialize/re-serialize round-trip under an explicit loader contract;
- deterministic sequence identity if append order must survive external storage;
- maliciously large provenance payload/resource-limit policy;
- exact-current-head execution on another environment;
- cross-language implementation agreement;
- human-factor testing for whether normalized position is misread as probability or truth;
- Windows validation on the intended local host.

Until performed, these remain `NOT_PROVEN`.

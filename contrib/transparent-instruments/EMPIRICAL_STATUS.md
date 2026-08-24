# Empirical Status — Transparent Instruments V0.1

Date: 2026-08-23

## What was executed

The exact reference implementation and unit-test logic in this directory were exercised before publication, then adversarially reviewed and re-tested after a non-finite-number defect was found and corrected.

Environment observed:

```text
PYTHON=3.13.5
OS=Linux 6.18.35 x86_64
EXTERNAL_PYTHON_DEPENDENCIES=NONE
UNIT_TESTS=18
PASS=18
FAIL=0
ERROR=0
```

A deterministic randomized invariant driver was then executed against the hardened implementation:

```text
SEED=20260823
ROUNDTRIP_CHECKS=10000
PROJECTION_CHECKS=5000
WEIGHTED_CHECKS=5000
ALIGNMENT_CHECKS=5000
TOTAL_RANDOMIZED_INVARIANT_CHECKS=25000
RESULT=PASS
```

The exact driver is `randomized_invariants.py` so the run can be reproduced rather than trusted as an uninspectable claim.

## Unit-test coverage

The 18-test suite covers:

1. scale normalization round-trip;
2. rejection of invalid scale bounds;
3. rejection of out-of-range observations;
4. rejection of NaN/infinite scale bounds;
5. rejection of NaN/infinite observed values;
6. rejection of booleans as numeric scale bounds;
7. Abacus append/latest behavior;
8. duplicate bead-ID rejection;
9. absence of implicit weighting;
10. deterministic explicit weighting;
11. missing weighted dimensions as an error;
12. rejection of NaN/infinite weights;
13. rejection of non-string bead identity;
14. explicit `authority = NONE` in snapshots;
15. Slide Ruler relative alignment;
16. required relation declaration;
17. rejection of non-text relation values;
18. projection that explicitly establishes neither semantic equivalence nor prediction.

## Randomized invariant coverage

The fixed-seed run checks implementation properties over arbitrary finite inputs:

- scale position/value round-trip remains bounded and numerically stable within an explicit floating-point tolerance;
- Slide Ruler projections remain inside the declared target scale and never flip their semantic-equivalence/prediction flags;
- explicitly weighted Abacus summaries remain within `[0, 1]` when component observations are on `[0, 1]` after normalization;
- alignment delta remains exactly defined as `left_position - right_position` within numerical tolerance and remains inside `[-1, 1]`.

This is implementation-invariant evidence, not statistical validation of any real-world metric.

## Defect found during recursive review

The first public draft passed 12 tests but ordinary Python comparisons do not reliably reject `NaN`. A non-finite scale/value/weight could therefore have produced a non-finite normalized or aggregate result.

Correction:

- finite numeric validation was added for scale bounds, observations, positions, and weights;
- booleans are rejected as numeric measurements;
- required provenance/relation fields must be non-empty strings;
- the expanded test suite now covers those failure cases.

The earlier 12-test result is historical evidence, not the current validation baseline.

## What this evidence supports

`PASS_REFERENCE_BEHAVIOR_V0_1_HARDENED`

Meaning: the current reference code behaved according to the 18 executable unit tests plus 25,000 deterministic randomized invariant checks in the recorded environment.

## What this evidence does not support

It does not establish:

- scientific validity of arbitrary dimensions;
- validity of any confidence estimate;
- correctness of a source observation;
- semantic equivalence between aligned scales;
- causal inference;
- predictive performance;
- permission or authority;
- Windows/macOS runtime compatibility;
- production readiness;
- security of a larger system embedding these objects.

## Failure-seeking next tests

Useful next work would attempt to break the model rather than add features:

- serialization round-trip;
- deterministic ordering across persistence layers;
- malformed or adversarial provenance strings beyond type/emptiness checks;
- explicit versioning of record shapes;
- cross-language implementation agreement;
- extreme but finite floating-point conditioning cases;
- human-factor tests for whether users misread normalized position as probability or truth.

Until those are performed, they remain `NOT_PROVEN`.

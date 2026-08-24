# Empirical Status — Transparent Instruments V0.1

Date: 2026-08-23

## What was executed

The exact reference implementation and unit-test logic in this directory were exercised before publication in an isolated Python environment.

Environment observed:

```text
PYTHON=3.13.5
OS=Linux 6.18.35 x86_64
EXTERNAL_PYTHON_DEPENDENCIES=NONE
UNIT_TESTS=12
PASS=12
FAIL=0
ERROR=0
```

The test suite covers:

1. scale normalization round-trip;
2. rejection of invalid scale bounds;
3. rejection of out-of-range observations;
4. Abacus append/latest behavior;
5. duplicate bead-ID rejection;
6. absence of implicit weighting;
7. deterministic explicit weighting;
8. missing weighted dimensions as an error;
9. explicit `authority = NONE` in snapshots;
10. Slide Ruler relative alignment;
11. required relation declaration;
12. projection that explicitly establishes neither semantic equivalence nor prediction.

## What this evidence supports

`PASS_REFERENCE_BEHAVIOR_V0_1`

Meaning: the reference code behaved according to these executable tests in the recorded environment.

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

- floating-point edge cases;
- NaN/infinity rejection policy;
- serialization round-trip;
- deterministic ordering across persistence layers;
- malicious or malformed provenance strings;
- explicit versioning of record shapes;
- cross-language implementation agreement;
- human-factor tests for whether users misread normalized position as probability or truth.

Until those are performed, they remain `NOT_PROVEN`.

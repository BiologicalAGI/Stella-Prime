# Empirical Status — Transparent Instruments V0.1

Date: 2026-08-23

## Current validation

The exact reference implementation and test logic were exercised before publication, adversarially reviewed, corrected after defects were found, and re-tested after each semantic change.

Environment observed:

```text
PYTHON=3.13.5
OS=Linux 6.18.35 x86_64
EXTERNAL_PYTHON_DEPENDENCIES=NONE
UNIT_TESTS=19
PASS=19
FAIL=0
ERROR=0
```

The deterministic randomized invariant suite was rerun against the current implementation:

```text
SEED=20260823
ROUNDTRIP_CHECKS=10000
PROJECTION_CHECKS=5000
WEIGHTED_CHECKS=5000
ALIGNMENT_CHECKS=5000
TOTAL_RANDOMIZED_INVARIANT_CHECKS=25000
RESULT=PASS
```

The exact randomized driver is `randomized_invariants.py` so the categories and seed are reproducible.

## Evidence history

### Pass 1 — initial implementation

```text
UNIT_TESTS=12
PASS=12
```

This was superseded by later failure-seeking evidence.

### Finding 1 — non-finite numeric contamination

Ordinary Python comparisons do not reliably reject `NaN`. A non-finite scale/value/weight could therefore have produced a non-finite normalized or aggregate result.

Correction:

- finite numeric validation was added for scale bounds, observations, positions, and weights;
- booleans are rejected as numeric measurements;
- required provenance/relation fields must be non-empty strings;
- the unit suite expanded to 18 tests.

### Finding 2 — append order could be mislabeled as temporal currentness

The earlier API used the name `latest(dimension)` while `Bead` also carries an `observed_at` field. The implementation actually selected the last bead **appended**, not the bead with the newest observed timestamp.

That behavior was deterministic, but the name could invite an unsupported currentness inference:

```text
LAST APPENDED != NEWEST OBSERVED TIME
```

A concrete backfill counterexample was tested:

1. append an observation labeled `2026-08-23T20:00:00-07:00`;
2. then append a backfilled observation labeled `2026-08-23T18:00:00-07:00`;
3. append order selects the second record even though its `observed_at` text denotes an earlier time.

Correction:

- `latest()` was replaced by `last_appended()`;
- `positions()` was replaced by `last_appended_positions()`;
- snapshot output now states:

```text
position_selection = LAST_APPENDED_PER_DIMENSION
observed_at_ordering = NOT_INTERPRETED
```

- `observed_at` remains provenance text; V0.1 does not parse or compare it;
- a regression test freezes this distinction;
- the current suite is 19/19 passing.

This correction is semantic hardening, not evidence that V0.1 implements a temporal currentness engine.

## Current unit-test coverage

The 19-test suite covers:

1. scale normalization round-trip;
2. rejection of invalid scale bounds;
3. rejection of out-of-range observations;
4. rejection of NaN/infinite scale bounds;
5. rejection of NaN/infinite observed values;
6. rejection of booleans as numeric scale bounds;
7. Abacus append/last-appended behavior;
8. explicit backfill test separating append order from observed-time currentness;
9. duplicate bead-ID rejection;
10. absence of implicit weighting;
11. deterministic explicit weighting;
12. missing weighted dimensions as an error;
13. rejection of NaN/infinite weights;
14. rejection of non-string bead identity;
15. explicit `authority = NONE` in snapshots;
16. Slide Ruler relative alignment;
17. required relation declaration;
18. rejection of non-text relation values;
19. projection that explicitly establishes neither semantic equivalence nor prediction.

## Randomized invariant coverage

The fixed-seed run checks implementation properties over arbitrary finite inputs:

- scale position/value round-trip remains bounded and numerically stable within an explicit floating-point tolerance;
- Slide Ruler projections remain inside the declared target scale and never flip their semantic-equivalence/prediction flags;
- explicitly weighted Abacus summaries remain within `[0, 1]` when component observations are on `[0, 1]` after normalization;
- alignment delta remains defined as `left_position - right_position` within numerical tolerance and remains inside `[-1, 1]`.

This is implementation-invariant evidence, not statistical validation of any real-world metric.

## What this evidence supports

`PASS_REFERENCE_BEHAVIOR_V0_1_SEMANTICALLY_HARDENED`

Meaning: the current reference code behaved according to 19 executable unit tests plus 25,000 deterministic randomized invariant checks in the recorded environment, and its append-order semantics no longer masquerade as observed-time currentness.

## What this evidence does not support

It does not establish:

- scientific validity of arbitrary dimensions;
- validity of any confidence estimate;
- correctness of a source observation;
- temporal ordering or currentness from `observed_at`;
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
- an explicit event/sequence identifier if persistent append order is required across stores;
- timestamp parsing/versioning only if temporal queries become an actual requirement;
- deterministic ordering across persistence layers;
- malformed or adversarial provenance strings beyond type/emptiness checks;
- explicit versioning of record shapes;
- cross-language implementation agreement;
- extreme but finite floating-point conditioning cases;
- human-factor tests for whether users misread normalized position as probability or truth.

Until those are performed, they remain `NOT_PROVEN`.

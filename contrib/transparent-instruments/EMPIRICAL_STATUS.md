# Empirical Status — Transparent Instruments V0.1

Date: 2026-08-23

## Current validation

The reference implementation has been repeatedly attacked, corrected, and rerun rather than treating the first green result as final truth.

Current environment observed:

```text
PYTHON=3.13.5
OS=Linux 6.18.35 x86_64
EXTERNAL_PYTHON_DEPENDENCIES=NONE
UNIT_TESTS=34
PASS=34
FAIL=0
ERROR=0
```

Current deterministic randomized invariant run:

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

Current public Git blob identities for the executed implementation/test/randomized artifacts:

```text
transparent_instruments.py = eebb37f8451846c75da734cd5379c1510eede3ae
test_transparent_instruments.py = ea34f03f2aaf629ec5d5db6be34a431b325f21da
randomized_invariants.py = 7cc7be093db27193d23a04904e44ac7ed0db39d1
```

The exact test blob differs from the pre-upload local draft only by blank-line formatting; its exact Git blob identity was reconstructed and the exact content passed 34/34 tests.

## Evidence history

### Pass 1 — initial implementation

```text
UNIT_TESTS=12
PASS=12
```

Superseded by later failure-seeking evidence.

### Finding 1 — non-finite numeric contamination

Ordinary comparisons do not reliably reject `NaN`. Non-finite scale values, observations, or weights could contaminate normalized/aggregate output.

Correction:

- reject NaN and infinities;
- reject booleans as numeric measurements;
- require non-empty required provenance/relation text.

### Finding 2 — append order could masquerade as temporal currentness

The earlier API name `latest()` selected the last **appended** bead while every bead also carries `observed_at` text. A backfilled older observation appended later therefore exposed an unsupported currentness implication.

Correction:

```text
latest() -> last_appended()
positions() -> last_appended_positions()
position_selection = LAST_APPENDED_PER_DIMENSION
observed_at_ordering = NOT_INTERPRETED
```

V0.1 preserves `observed_at` as provenance text and does not parse or compare timestamps.

### Finding 3 — finite inputs could still overflow intermediate arithmetic

The prior normalization formula used:

```text
(value - minimum) / (maximum - minimum)
```

For the valid finite scale `[-1e308, +1e308]`, `maximum - minimum` overflows. Direct reproduction showed:

```text
position(0.0)      -> 0.0   # should be 0.5
position(1e308)    -> NaN
value_at(0.5)      -> inf
```

Likewise, two valid weights of `1e308` could overflow the weight sum and produce a wrong aggregate.

Correction:

- scale normalization now divides endpoints/value by a common finite magnitude before differencing;
- interpolation uses a convex combination instead of subtracting the full range;
- explicit weighting rescales all weights by the maximum weight before `math.fsum` aggregation;
- integers that cannot be represented exactly as float are rejected rather than silently rounded;
- randomized coverage now includes 10,000 extreme finite scales spanning subnormal through near-maximum exponents and weights spanning approximately `1e-300` through `1e308`.

### Finding 4 — receipt integrity was only guaranteed on the intended constructor path

Earlier `Alignment` and `Projection` dataclasses exposed derived fields directly. A caller could instantiate a receipt with an arbitrary projected value/delta and could even set non-claim flags such as `predictive_claim=True` before serialization.

Correction:

- Alignment positions/delta are derived properties;
- Projection source position/projected value are derived properties;
- semantic-equivalence and predictive-claim flags are fixed derived false properties;
- derived fields cannot be injected through constructors;
- receipts include the declared scales/values necessary to recompute their numeric result;
- strict JSON serialization is tested with `allow_nan=False`;
- records expose `schema_version = transparent-instruments/0.1`;
- validated numeric inputs are stored canonically as finite floats;
- optional scale metadata and notes are required to be text.

### Independent GitHub Copilot review

A manually requested GitHub Copilot code review on PR #2 reviewed all seven changed files and returned a COMMENTED review recommending approval with two improvement comments.

The comments identified:

1. validated Scale endpoints should be canonicalized into stored floats;
2. weighted lookup should avoid rescanning all beads once per requested dimension.

Both were addressed on later commits. Copilot's review is advisory only and is not treated as approval or merge authority.

## Current unit-test coverage

The 34-test suite now covers:

- ordinary and extreme scale normalization/interpolation;
- invalid/out-of-range/non-finite/unrepresentable numeric inputs;
- canonical float storage and text-only metadata boundaries;
- append-order semantics and backfill/currentness separation;
- duplicate/non-Bead rejection;
- explicit-only weighting, missing dimensions, non-finite weights, and extreme finite weights;
- schema version and `authority = NONE` snapshot declarations;
- strict JSON snapshot serialization;
- relative alignment and projection non-claim semantics;
- self-reproducible Alignment and Projection receipts;
- prevention of caller injection of derived receipt fields/claims.

## Randomized invariant coverage

The fixed-seed run checks:

- 10,000 ordinary scale round trips;
- 10,000 extreme finite scale interpolation/normalization cases;
- 5,000 Slide Ruler projections;
- 5,000 weighted Abacus runs over a very wide finite weight range;
- 5,000 Alignment delta checks.

This is implementation-invariant evidence, not validation of any real-world metric or interpretation.

## What this evidence supports

`PASS_REFERENCE_BEHAVIOR_V0_1_RECEIPT_HARDENED`

Meaning: the current public implementation behaves according to 34 executable unit tests and 35,000 deterministic randomized invariant checks in the recorded environment, including explicit extreme-range arithmetic and receipt-integrity regressions.

## What this evidence does not support

It does not establish:

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

Useful next work should continue trying to falsify assumptions rather than adding features:

- persistence/deserialize/re-serialize round-trip under an explicit loader contract;
- deterministic sequence identity if append order must survive external storage;
- maliciously large provenance payload/resource-limit policy;
- cross-language implementation agreement;
- human-factor testing for whether normalized position is misread as probability or truth;
- Windows validation on the intended local host.

Until performed, these remain `NOT_PROVEN`.

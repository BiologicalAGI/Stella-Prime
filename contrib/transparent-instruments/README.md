# Transparent Instruments — Abacus + Slide Ruler V0.1

Status: **PUBLIC DRAFT / REFERENCE IMPLEMENTATION / NON-AUTHORITATIVE**

This small toolkit explores two deliberately transparent reasoning instruments:

- **Abacus** — an append-only board of provenance-carrying observations across named dimensions.
- **Slide Ruler** — a continuous-scale alignment/comparison instrument whose receipts expose the declared scales, values, relation, and justification needed to reproduce the numeric result.

The goal is not to create another autonomous decision engine. The goal is to make measurement, normalization, weighting, comparison, provenance, and ordering assumptions inspectable enough that a human or larger system can see exactly what was done.

## Design laws

```text
MEASUREMENT != INTERPRETATION
NORMALIZATION != TRUTH
WEIGHTED SCORE != AUTHORITY
ALIGNMENT != EQUIVALENCE
PROJECTION != PREDICTION
CAPABILITY != PERMISSION
OBSERVED THEN != TRUE NOW
APPEND ORDER != OBSERVED-TIME CURRENTNESS
FINITE INPUT != SAFE INTERMEDIATE ARITHMETIC
SERIALIZED RECEIPT != TRUSTED CLAIM
```

## Lineage

**Abacus has prior project lineage.** Earlier private work used dimensional-abacus ideas for indexing/state mapping and later for governance/review boundaries. A separate private `TCV_ABACUS_Universal` laboratory also contains a larger local-first application scaffold. This public draft does **not** claim that those larger experimental systems are validated or production-ready.

**Slide Ruler is new in this pass.** No earlier repository occurrence of `Slide Ruler` or `slide rule` was found during the 2026-08-23 recursive review. It is introduced here as a simpler companion instrument: Abacus tracks discrete observations on declared dimensions; Slide Ruler exposes continuous relative placement across declared scales.

## Abacus

A `Bead` contains:

- stable `bead_id`;
- named `dimension`;
- finite numeric `value`;
- explicitly declared `Scale`;
- `basis`;
- `source`;
- `observed_at` provenance text;
- optional text note.

The Abacus reports the **last-appended** position for each dimension and computes an explicitly weighted summary only when the caller supplies the weights. There is no implicit weighting and no authority decision attached to the resulting number.

`observed_at` is not parsed or sorted in V0.1. Snapshots therefore declare:

```text
position_selection = LAST_APPENDED_PER_DIMENSION
observed_at_ordering = NOT_INTERPRETED
```

The implementation also rejects NaN/infinity, booleans-as-numbers, and integer values that cannot be represented exactly as the float arithmetic used by this reference.

## Slide Ruler

The Slide Ruler can:

1. align two observations by relative position on their declared scales;
2. report the positional delta;
3. project one normalized position onto another declared scale when a relation and justification are supplied.

Alignment and Projection receipts include their scale definitions and raw values so the numeric result can be recomputed from the receipt itself.

Derived values are not caller-controlled receipt fields. In particular:

```text
semantic_equivalence_established = false
predictive_claim = false
```

are derived non-claims. A caller cannot inject a different projected value/delta/claim through the normal dataclass constructor.

Every serialized record uses:

```text
schema_version = transparent-instruments/0.1
```

## Numeric hardening

Finite endpoints do not guarantee safe intermediate subtraction. For example, `(+1e308) - (-1e308)` overflows despite both endpoints being finite.

V0.1 therefore:

- normalizes after scaling values/endpoints by a common magnitude;
- interpolates with a convex combination instead of subtracting the full range;
- rescales explicit weights before `math.fsum` aggregation;
- tests extreme finite values across the representable exponent range.

## Quick start

No external packages are required.

```bash
cd contrib/transparent-instruments
python -m unittest -v test_transparent_instruments.py
python randomized_invariants.py
python example.py
```

## Empirical status

Current validation on 2026-08-23 in Python **3.13.5**, Linux x86_64:

```text
UNIT_TESTS=34
PASS=34
FAIL=0
ERROR=0

SEED=20260823
ROUNDTRIP_CHECKS=10000
EXTREME_SCALE_CHECKS=10000
PROJECTION_CHECKS=5000
WEIGHTED_CHECKS=5000
ALIGNMENT_CHECKS=5000
TOTAL_RANDOMIZED_INVARIANT_CHECKS=35000
RESULT=PASS
```

The failure history is intentionally preserved. Earlier green states were superseded after review found:

1. non-finite numeric contamination;
2. append-order/currentness ambiguity;
3. extreme finite intermediate overflow and weight-sum overflow;
4. forgeable/incomplete standalone receipt fields.

An independent GitHub Copilot code review also identified canonical numeric storage and an avoidable repeated bead scan; both were corrected. Copilot's review is advisory and does not count as merge authority.

This evidence proves bounded implementation behavior only. It does **not** prove:

- Windows compatibility;
- scientific/statistical validity of a chosen dimension;
- correctness of supplied evidence;
- temporal currentness;
- semantic comparability of two scales;
- predictive power;
- safety of a larger embedding system;
- authorization to act.

See `EMPIRICAL_STATUS.md` for the exact defect history, Git blob identities, proof boundary, and remaining failure-seeking work.

## Why this exists

A recurring failure mode in AI-assisted and human-built systems is to collapse several different things into one opaque score:

```text
observation
+ interpretation
+ weighting
+ confidence
+ authority
= one number that looks objective
```

This reference takes the opposite approach. The numeric mechanics are intentionally small; provenance, reproducibility, and non-equivalence rules are first-class.

## What this is not

- not an LLM;
- not a confidence oracle;
- not a safety classifier;
- not a permission system;
- not a temporal currentness engine;
- not a statistical package;
- not a substitute for domain validation;
- not a claim that historical Abacus experiments are proven.

## Files

- `transparent_instruments.py` — dependency-free reference implementation.
- `test_transparent_instruments.py` — executable unit tests.
- `randomized_invariants.py` — fixed-seed randomized invariant checks.
- `example.py` — minimal usage example.
- `EMPIRICAL_STATUS.md` — proof boundary, defect history, and validation receipts.
- `LICENSE_STATUS.md` — licensing hold for this public draft.

## Contribution posture

This code is publicly inspectable before any claim of maturity. Counterexamples and tests that break an assumption are more useful than praise.

A future version should stay small unless empirical use demonstrates that additional machinery is necessary.

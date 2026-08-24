# Transparent Instruments — Abacus + Slide Ruler V0.1

Status: **PUBLIC DRAFT / REFERENCE IMPLEMENTATION / NON-AUTHORITATIVE**

This small toolkit explores two deliberately transparent reasoning instruments:

- **Abacus** — an append-only board of provenance-carrying observations across named dimensions.
- **Slide Ruler** — a continuous-scale alignment/comparison instrument that exposes its relation and justification instead of silently asserting that unlike scales are equivalent.

The goal is not to create another autonomous decision engine. The goal is to make measurement, normalization, weighting, comparison, and provenance inspectable enough that a human or larger system can see exactly what was done.

## Design laws

```text
MEASUREMENT != INTERPRETATION
NORMALIZATION != TRUTH
WEIGHTED SCORE != AUTHORITY
ALIGNMENT != EQUIVALENCE
PROJECTION != PREDICTION
CAPABILITY != PERMISSION
OBSERVED THEN != TRUE NOW
```

## Lineage

**Abacus has prior project lineage.** Earlier private work used dimensional-abacus ideas for indexing/state mapping and later for governance/review boundaries. A separate private `TCV_ABACUS_Universal` laboratory also contains a larger local-first application scaffold. This public draft does **not** claim that those larger experimental systems are validated or production-ready.

**Slide Ruler is new in this pass.** No earlier repository occurrence of `Slide Ruler` or `slide rule` was found during the 2026-08-23 recursive review. It is introduced here as a simpler companion instrument: Abacus tracks discrete observations on declared dimensions; Slide Ruler exposes continuous relative placement across declared scales.

## Abacus

A `Bead` contains:

- stable `bead_id`
- named `dimension`
- raw numeric `value`
- explicitly declared `Scale`
- `basis`
- `source`
- `observed_at`
- optional note

The Abacus is append-only in memory. It can report latest positions and can calculate an explicitly weighted summary **only when the caller supplies the weights**. There is no implicit weighting and no authority decision attached to the resulting number.

Non-finite numbers (`NaN`, positive/negative infinity) and booleans-as-numbers are rejected rather than allowed to silently contaminate normalized or weighted results.

## Slide Ruler

The Slide Ruler can:

1. align two observations by their normalized positions on their own declared scales;
2. report the positional difference;
3. project one normalized position onto another declared numeric scale when the caller supplies a named relation and justification.

A projection explicitly reports:

```text
semantic_equivalence_established = false
predictive_claim = false
```

The math may be valid while the semantics are invalid. The tool refuses to hide that distinction.

## Quick start

No external packages are required.

```bash
cd contrib/transparent-instruments
python -m unittest -v test_transparent_instruments.py
python example.py
```

## Empirical status

Validated on 2026-08-23 in a Python **3.13.5**, Linux x86_64 sandbox.

Initial pass:

```text
UNIT_TESTS=12
PASS=12
```

A recursive failure-seeking review then found a non-finite-number edge case, corrected it, expanded validation, and established the current baseline:

```text
UNIT_TESTS=18
PASS=18
FAIL=0
ERROR=0
```

This proves only that the current reference implementation behaves as specified by those tests in that environment. It does **not** prove:

- Windows compatibility;
- statistical validity of a chosen dimension;
- correctness of human-supplied evidence;
- semantic comparability of two scales;
- predictive power;
- safety of decisions made by a larger system;
- authorization to act.

See `EMPIRICAL_STATUS.md` for the defect history, exact proof boundary, and next failure-seeking tests.

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

This reference takes the opposite approach. The numeric mechanics are intentionally small; provenance and non-equivalence rules are first-class.

## What this is not

- not an LLM
- not a confidence oracle
- not a safety classifier
- not a permission system
- not a statistical package
- not a substitute for domain validation
- not a claim that historical Abacus experiments are proven

## Files

- `transparent_instruments.py` — dependency-free reference implementation.
- `test_transparent_instruments.py` — executable unit tests.
- `example.py` — minimal usage example.
- `EMPIRICAL_STATUS.md` — proof boundary, defect history, and current validation record.
- `LICENSE_STATUS.md` — licensing hold for this public draft.

## Contribution posture

This code is being made publicly inspectable before any claim of maturity. Findings, counterexamples, simpler formulations, and tests that break an assumption are more useful than praise.

A future version should stay small unless empirical use demonstrates that additional machinery is necessary.

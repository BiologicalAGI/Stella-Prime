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
LINEAR SCALE != GENERIC SCALE
COMPENSATORY AGGREGATE != DECISION AUTHORITY
```

## Lineage

**Abacus has prior project lineage.** Earlier private work used dimensional-abacus ideas for indexing/state mapping and later for governance/review boundaries. A separate private `TCV_ABACUS_Universal` laboratory also contains a larger local-first application scaffold. This public draft does **not** claim that those larger experimental systems are validated or production-ready.

**Slide Ruler is new in this pass.** No earlier repository occurrence of `Slide Ruler` or `slide rule` was found during the 2026-08-23 recursive review. It is introduced here as a simpler companion instrument: Abacus tracks discrete observations on declared dimensions; Slide Ruler exposes continuous relative placement across declared scales.

## Scale contract

V0.1 supports one explicit scale model:

```text
SCALE_MODEL = LINEAR_MIN_MAX
```

That is intentional. This implementation does not silently reinterpret logarithmic, ordinal, categorical, or other scale semantics as linear min-max normalization. An unsupported model is rejected.

Finite numeric endpoints are not enough to guarantee safe intermediate arithmetic, so normalization and interpolation are implemented to avoid full-range overflow on extreme finite endpoints such as `[-1e308,+1e308]`.

## Abacus

A `Bead` contains:
- stable `bead_id`;
- named `dimension`;
- finite numeric `value`;
- explicitly declared linear `Scale`;
- `basis`;
- `source`;
- `observed_at` provenance text;
- optional text note.

The Abacus reports the **last-appended** position for each dimension. `observed_at` is not parsed or sorted in V0.1, so snapshots explicitly state:

```text
position_selection = LAST_APPENDED_PER_DIMENSION
observed_at_ordering = NOT_INTERPRETED
```

## Explicit weighting

The supported aggregation model is named rather than implied:

```text
WEIGHTED_AGGREGATION_MODEL = COMPENSATORY_WEIGHTED_MEAN
```

A compensatory weighted mean can trade a lower dimension against a higher one. That mathematical property is not a safety rule, a veto rule, a scientific model, or decision authority.

There is no implicit weighting. The caller must provide weights explicitly.

For auditability, `explicit_weighted_receipt()` preserves:
- canonical sorted dimensions;
- selected last-appended bead IDs;
- normalized positions;
- canonical finite weights;
- the scale and aggregation model names;
- selection rule;
- resulting weighted position;
- schema version;
- `authority = NONE`.

The convenience `explicit_weighted_position()` returns only the numeric value derived from that same receipt path.

## Slide Ruler

The Slide Ruler can:
1. align two observations by relative position on their declared linear scales;
2. report the positional delta;
3. project one normalized position onto another declared linear scale when a relation and justification are supplied.

Alignment and Projection receipts include their scale definitions and raw values so the numeric result can be recomputed from the receipt itself.

Derived values are not caller-controlled receipt fields. In particular:

```text
semantic_equivalence_established = false
predictive_claim = false
```

are derived non-claims.

Every serialized record uses:

```text
schema_version = transparent-instruments/0.1
```

## Quick start

No external packages are required.

```bash
cd contrib/transparent-instruments
python -m unittest -v test_transparent_instruments.py
python randomized_invariants.py
python example.py
```

## Empirical status

The current locally executed candidate was validated on 2026-08-23 in Python **3.13.5**, Linux x86_64:

```text
UNIT_TESTS=38
PASS=38
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

The repository currently has no GitHub Actions run for the exact newest PR head. Therefore this is stated as **local reference-candidate evidence**, not remote exact-head CI evidence.

Failure-seeking has already found and corrected:
1. non-finite numeric contamination;
2. append-order/currentness ambiguity;
3. extreme finite intermediate arithmetic and large-weight overflow;
4. forgeable/incomplete derived receipt fields;
5. hidden linear-scale and compensatory-aggregation assumptions.

An independent GitHub Copilot review on an earlier head also identified canonical numeric storage and an avoidable repeated bead scan; both were corrected. Copilot review is advisory and does not count as merge authority.

This evidence proves bounded implementation behavior only. It does **not** prove:
- Windows/macOS compatibility;
- scientific/statistical validity of a dimension;
- correctness of supplied evidence;
- temporal currentness;
- semantic comparability of two scales;
- predictive power;
- safety of a larger embedding system;
- authorization to act.

See `EMPIRICAL_STATUS.md` for the defect history, current Git blob identities, proof boundary, and remaining failure-seeking work.

## What this is not

- not an LLM;
- not a confidence oracle;
- not a safety classifier;
- not a permission system;
- not a temporal currentness engine;
- not a generic scale framework;
- not a statistical validation package;
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

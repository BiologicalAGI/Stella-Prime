# Transparent Instruments — Abacus + Slide Ruler V0.1

Status: **PUBLIC DRAFT / TESTED REFERENCE / NON-AUTHORITATIVE**

This small toolkit explores two deliberately transparent reasoning instruments:

- **Abacus** — a board of provenance-carrying observations whose **public mutation API is append-only**.
- **Slide Ruler** — a continuous-scale alignment/comparison instrument whose receipts expose the declared scales, values, relation, and justification needed to reproduce the numeric result.

The goal is not to create another autonomous decision engine. The goal is to make measurement, normalization, weighting, comparison, provenance, storage assumptions, and ordering assumptions inspectable enough that a human or larger system can see exactly what was done.

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
PUBLIC API APPEND-ONLY != TAMPER-PROOF MEMORY
```

## Lineage

**Abacus has prior project lineage.** Earlier private work used dimensional-abacus ideas for indexing/state mapping and later for governance/review boundaries. A separate private `TCV_ABACUS_Universal` laboratory also contains a larger local-first application scaffold. This public draft does **not** claim that those larger experimental systems are validated or production-ready.

**Slide Ruler is new in this pass.** No earlier repository occurrence of `Slide Ruler` or `slide rule` was found during the 2026-08-23 recursive review. It is introduced here as a simpler companion instrument: Abacus tracks discrete observations on declared dimensions; Slide Ruler exposes continuous relative placement across declared scales.

## Scale contract

V0.1 supports one explicit scale model:

```text
SCALE_MODEL = LINEAR_MIN_MAX
```

This implementation does not silently reinterpret logarithmic, ordinal, categorical, or other scale semantics as linear min-max normalization. An unsupported model is rejected.

The numerical implementation has two paths:

- direct finite-width subtraction for narrow/ordinary intervals, preserving relative precision;
- scale-relative arithmetic only when the full interval width would overflow.

Interpolation uses a convex combination with `math.fsum`. The failure-seeking suite includes both extreme finite ranges such as `[-1e308,+1e308]` and narrow ULP-scale intervals.

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
storage_contract = PUBLIC_API_APPEND_ONLY_NOT_TAMPER_PROOF
```

The public API exposes `add()` but no remove/replace operation. This is an application-level API contract, **not** a security boundary against Python code that directly manipulates private attributes or process memory.

## Explicit weighting

The supported aggregation model is named rather than implied:

```text
WEIGHTED_AGGREGATION_MODEL = COMPENSATORY_WEIGHTED_MEAN
```

A compensatory weighted mean can trade a lower dimension against a higher one. That mathematical property is not a safety rule, veto rule, scientific model, or decision authority.

There is no implicit weighting. The caller must provide weights explicitly.

For auditability, `explicit_weighted_receipt()` preserves:
- canonical sorted dimensions;
- full selected bead receipts, including basis/source/scale/value;
- selected bead IDs;
- normalized positions;
- canonical finite weights;
- scale and aggregation model names;
- selection rule;
- resulting weighted position;
- schema version;
- `authority = NONE`.

The convenience `explicit_weighted_position()` returns only the normalized weighted position derived from that same receipt path.

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

No external Python packages are required.

```bash
cd contrib/transparent-instruments
python -m unittest -v test_transparent_instruments.py
python randomized_invariants.py
python example.py
```

## Current empirical status

GitHub Actions run `32686643871` executed the PR merge candidate across six GitHub-hosted environments:

```text
ubuntu-latest / Python 3.12  PASS
ubuntu-latest / Python 3.13  PASS
windows-latest / Python 3.12 PASS
windows-latest / Python 3.13 PASS
macos-latest / Python 3.12   PASS
macos-latest / Python 3.13   PASS
```

Each matrix job ran the same unit and invariant commands. A completed Ubuntu/Python 3.13 log records:

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

This establishes cross-platform behavior on GitHub-hosted CPython 3.12/3.13 for the tested merge candidate. It does **not** establish the current iBUYPOWER host, all Python implementations, scientific validity, production readiness, or permission to act.

Failure-seeking has already found and corrected:
1. non-finite numeric contamination;
2. append-order/currentness ambiguity;
3. extreme finite intermediate arithmetic and large-weight overflow;
4. forgeable/incomplete derived receipt fields;
5. hidden linear-scale and compensatory-aggregation assumptions;
6. precision loss on narrow same-sign intervals caused by using overflow-protection arithmetic universally;
7. overbroad append-only wording and insufficient weighted-receipt provenance.

Independent GitHub Copilot reviews also identified canonical numeric storage, repeated bead scans, duplicated derived receipt literals, stale validation metadata, and minor execution/documentation ergonomics. Concrete findings were either corrected or explicitly bounded. Copilot review is advisory and does not count as merge authority.

See `EMPIRICAL_STATUS.md` for the evidence history, proof boundary, and remaining holds.

## What this is not

- not an LLM;
- not a confidence oracle;
- not a safety classifier;
- not a permission system;
- not a temporal currentness engine;
- not a generic scale framework;
- not a tamper-proof append-only ledger;
- not a statistical validation package;
- not a substitute for domain validation;
- not a claim that historical Abacus experiments are proven.

## Files

- `transparent_instruments.py` — dependency-free reference implementation.
- `test_transparent_instruments.py` — executable unit tests.
- `randomized_invariants.py` — fixed-seed deterministic invariant checks.
- `example.py` — minimal usage example.
- `EMPIRICAL_STATUS.md` — proof boundary, defect history, and validation receipts.
- `LICENSE_STATUS.md` — licensing hold for this public draft.
- `.github/workflows/transparent-instruments-ci.yml` — read-only cross-platform CI for this contribution.

## Contribution posture

This code is publicly inspectable before any claim of maturity. Counterexamples and tests that break an assumption are more useful than praise.

A future version should stay small unless empirical use demonstrates that additional machinery is necessary.

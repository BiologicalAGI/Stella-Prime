"""Deterministic randomized invariant checks for Transparent Instruments V0.1."""
import math
import random

from transparent_instruments import Abacus, Bead, Scale, SlideRuler

SEED = 20260823


def _random_finite_float() -> float:
    """Generate a finite float spanning subnormal through near-max exponents."""
    exponent = random.randint(-1074, 1023)
    mantissa = max(random.random(), 2**-53)
    value = math.ldexp(mantissa, exponent)
    if not math.isfinite(value):
        value = math.nextafter(math.inf, 0.0)
    if random.random() < 0.5:
        value = -value
    return value


def main() -> None:
    random.seed(SEED)
    roundtrip_checks = 0
    extreme_scale_checks = 0
    projection_checks = 0
    weighted_checks = 0
    alignment_checks = 0

    for _ in range(10_000):
        lo = random.uniform(-1e9, 1e9)
        span = 10 ** random.uniform(-6, 9)
        hi = lo + span
        if not hi > lo:
            hi = math.nextafter(lo, math.inf)

        scale = Scale(lo, hi)
        position = random.random()
        value = scale.value_at(position)
        recovered_position = scale.position(value)

        if not 0.0 <= recovered_position <= 1.0:
            raise AssertionError("normalized position escaped [0, 1]")

        recovered_value = scale.value_at(recovered_position)
        absolute_tolerance = max(
            1e-12,
            math.ulp(value) * 4 if value != 0 else 1e-12,
        )
        if not math.isclose(
            recovered_value,
            value,
            rel_tol=1e-12,
            abs_tol=absolute_tolerance,
        ):
            raise AssertionError("scale round-trip exceeded tolerance")
        roundtrip_checks += 1

    for _ in range(10_000):
        left = _random_finite_float()
        right = _random_finite_float()
        if left == right:
            continue
        lo, hi = sorted((left, right))
        scale = Scale(lo, hi)
        position = random.random()
        value = scale.value_at(position)
        recovered_position = scale.position(value)

        if not math.isfinite(value):
            raise AssertionError("extreme scale interpolation became non-finite")
        if not math.isfinite(recovered_position):
            raise AssertionError("extreme normalized position became non-finite")
        if not 0.0 <= recovered_position <= 1.0:
            raise AssertionError("extreme normalized position escaped [0, 1]")
        extreme_scale_checks += 1

    for _ in range(5_000):
        lo_from = random.uniform(-1e6, 1e6)
        hi_from = lo_from + random.uniform(1e-3, 1e6)
        lo_to = random.uniform(-1e6, 1e6)
        hi_to = lo_to + random.uniform(1e-3, 1e6)
        from_scale = Scale(lo_from, hi_from)
        to_scale = Scale(lo_to, hi_to)

        source_value = from_scale.value_at(random.random())
        result = SlideRuler.project(
            source_value,
            from_scale=from_scale,
            to_scale=to_scale,
            relation="deterministic randomized same-position check",
            justification="verify projection bounds and non-claim flags",
        )

        if not lo_to <= result.projected_value <= hi_to:
            raise AssertionError("projection escaped target scale")
        if result.semantic_equivalence_established or result.predictive_claim:
            raise AssertionError("projection asserted a prohibited semantic claim")
        projection_checks += 1

    for run_index in range(5_000):
        abacus = Abacus()
        weights: dict[str, float] = {}

        for dimension_index in range(random.randint(1, 8)):
            dimension = f"d{dimension_index}"
            abacus.add(
                Bead(
                    bead_id=f"weighted.{run_index}.{dimension_index}",
                    dimension=dimension,
                    value=random.uniform(0, 100),
                    scale=Scale(0, 100),
                    basis="deterministic randomized invariant test",
                    source=f"seed-{SEED}",
                    observed_at=f"run-{run_index}.{dimension_index}",
                )
            )
            # Exercise a wide finite dynamic range without allowing infinity.
            weights[dimension] = 10.0 ** random.uniform(-300, 308)

        result = abacus.explicit_weighted_position(weights)
        if not 0.0 <= result <= 1.0:
            raise AssertionError("weighted position escaped [0, 1]")
        if not math.isfinite(result):
            raise AssertionError("weighted position became non-finite")
        weighted_checks += 1

    for run_index in range(5_000):
        left_position = random.random()
        right_position = random.random()

        left = Bead(
            bead_id=f"left.{run_index}",
            dimension="left",
            value=left_position,
            scale=Scale(0, 1),
            basis="deterministic randomized invariant test",
            source=f"seed-{SEED}",
            observed_at=f"left-{run_index}",
        )
        right = Bead(
            bead_id=f"right.{run_index}",
            dimension="right",
            value=right_position,
            scale=Scale(0, 1),
            basis="deterministic randomized invariant test",
            source=f"seed-{SEED}",
            observed_at=f"right-{run_index}",
        )

        result = SlideRuler.align(
            left,
            right,
            relation="deterministic randomized relative-position check",
            justification="verify delta definition and bounds",
        )

        if not math.isclose(
            result.position_delta,
            left_position - right_position,
            rel_tol=0.0,
            abs_tol=1e-15,
        ):
            raise AssertionError("alignment delta did not equal left minus right")
        if not -1.0 <= result.position_delta <= 1.0:
            raise AssertionError("alignment delta escaped [-1, 1]")
        alignment_checks += 1

    total = (
        roundtrip_checks
        + extreme_scale_checks
        + projection_checks
        + weighted_checks
        + alignment_checks
    )
    print(f"SEED={SEED}")
    print(f"ROUNDTRIP_CHECKS={roundtrip_checks}")
    print(f"EXTREME_SCALE_CHECKS={extreme_scale_checks}")
    print(f"PROJECTION_CHECKS={projection_checks}")
    print(f"WEIGHTED_CHECKS={weighted_checks}")
    print(f"ALIGNMENT_CHECKS={alignment_checks}")
    print(f"TOTAL_RANDOMIZED_INVARIANT_CHECKS={total}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()

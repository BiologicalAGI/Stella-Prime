from transparent_instruments import Abacus, Bead, Scale, SlideRuler

percent = Scale(0, 100, "%", "observed score")
risk_band = Scale(0, 5, "band", "risk band")

abacus = Abacus()
abacus.add(
    Bead(
        bead_id="run-001.clarity",
        dimension="clarity",
        value=82,
        scale=percent,
        basis="human-scored fixture result",
        source="fixture/run-001",
        observed_at="2026-08-23T19:00:00-07:00",
    )
)
abacus.add(
    Bead(
        bead_id="run-001.traceability",
        dimension="traceability",
        value=74,
        scale=percent,
        basis="receipt completeness check",
        source="fixture/run-001",
        observed_at="2026-08-23T19:00:01-07:00",
    )
)

print(abacus.snapshot())

# Explicit weighting is allowed only when the caller supplies it.
print(
    "weighted position:",
    abacus.explicit_weighted_position({"clarity": 1, "traceability": 1}),
)

# Slide Ruler projection is mathematical alignment only. Its receipt carries
# the scale definitions and schema version needed to recompute the result.
projection = SlideRuler.project(
    82,
    from_scale=percent,
    to_scale=risk_band,
    relation="demonstration of same normalized position",
    justification="show mechanics; no semantic equivalence claimed",
)
print(projection.to_dict())

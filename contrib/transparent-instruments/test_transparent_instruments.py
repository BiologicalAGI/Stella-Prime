import json
import unittest

from transparent_instruments import (
    SCHEMA_VERSION,
    SCALE_MODEL,
    STORAGE_CONTRACT,
    WEIGHTED_AGGREGATION_MODEL,
    Abacus,
    Alignment,
    Bead,
    Projection,
    Scale,
    SlideRuler,
)


class ScaleTests(unittest.TestCase):
    def test_position_and_value_round_trip(self):
        scale = Scale(0, 100, "%", "percent")
        self.assertAlmostEqual(scale.position(25), 0.25)
        self.assertAlmostEqual(scale.value_at(0.25), 25)

    def test_invalid_scale_rejected(self):
        with self.assertRaises(ValueError):
            Scale(1, 1)

    def test_out_of_range_value_rejected(self):
        scale = Scale(0, 10)
        with self.assertRaises(ValueError):
            scale.position(11)

    def test_non_finite_scale_rejected(self):
        with self.assertRaises(ValueError):
            Scale(0, float("nan"))
        with self.assertRaises(ValueError):
            Scale(0, float("inf"))

    def test_non_finite_value_rejected(self):
        scale = Scale(0, 10)
        with self.assertRaises(ValueError):
            scale.position(float("nan"))
        with self.assertRaises(ValueError):
            scale.position(float("inf"))

    def test_boolean_numeric_values_rejected(self):
        with self.assertRaises(ValueError):
            Scale(False, 1)

    def test_unrepresentable_integer_rejected(self):
        with self.assertRaises(ValueError):
            Scale(0, 10**10_000)
        with self.assertRaises(ValueError):
            Scale(0, 2**53 + 1)

    def test_exact_integer_inputs_are_canonicalized_to_float(self):
        scale = Scale(0, 100)
        self.assertIs(type(scale.minimum), float)
        self.assertIs(type(scale.maximum), float)
        self.assertEqual(scale.minimum, 0.0)
        self.assertEqual(scale.maximum, 100.0)

    def test_scale_metadata_must_be_text(self):
        with self.assertRaises(ValueError):
            Scale(0, 1, unit=object())
        with self.assertRaises(ValueError):
            Scale(0, 1, label=object())

    def test_scale_declares_linear_min_max_model(self):
        scale = Scale(0, 100)
        self.assertEqual(scale.model, SCALE_MODEL)
        self.assertEqual(scale.model, "LINEAR_MIN_MAX")

    def test_unsupported_scale_model_rejected(self):
        with self.assertRaises(ValueError):
            Scale(1, 100, model="LOGARITHMIC")

    def test_extreme_finite_scale_normalizes_without_overflow(self):
        scale = Scale(-1e308, 1e308)
        self.assertEqual(scale.position(-1e308), 0.0)
        self.assertEqual(scale.position(0.0), 0.5)
        self.assertEqual(scale.position(1e308), 1.0)

    def test_extreme_finite_scale_interpolates_without_overflow(self):
        scale = Scale(-1e308, 1e308)
        self.assertEqual(scale.value_at(0.0), -1e308)
        self.assertEqual(scale.value_at(0.5), 0.0)
        self.assertEqual(scale.value_at(1.0), 1e308)

    def test_narrow_same_sign_interval_preserves_relative_position(self):
        scale = Scale(-1.000000000000013e-10, -1e-10)
        value = -1.0000000000000007e-10
        self.assertEqual(scale.position(value), 0.95)


class AbacusTests(unittest.TestCase):
    def setUp(self):
        self.scale = Scale(0, 100, "%")
        self.clarity = Bead(
            "b.clarity.001",
            "clarity",
            80,
            self.scale,
            "observed test result",
            "fixture-A",
            "2026-08-23T19:00:00-07:00",
        )
        self.traceability = Bead(
            "b.trace.001",
            "traceability",
            60,
            self.scale,
            "observed test result",
            "fixture-A",
            "2026-08-23T19:00:01-07:00",
        )

    def test_bead_value_is_canonical_float(self):
        self.assertIs(type(self.clarity.value), float)
        self.assertEqual(self.clarity.value, 80.0)

    def test_optional_note_must_be_text(self):
        with self.assertRaises(ValueError):
            Bead(
                "b.bad.note",
                "clarity",
                80,
                self.scale,
                "basis",
                "source",
                "observed",
                note=object(),
            )

    def test_bead_requires_declared_scale(self):
        with self.assertRaises(ValueError):
            Bead(
                "b.bad.scale",
                "clarity",
                80,
                object(),
                "basis",
                "source",
                "observed",
            )

    def test_append_and_last_appended(self):
        abacus = Abacus([self.clarity])
        self.assertEqual(abacus.last_appended("clarity"), self.clarity)
        self.assertIsNone(abacus.last_appended("unknown"))

    def test_append_order_does_not_claim_observed_time_currentness(self):
        newer = Bead(
            "b.clarity.newer",
            "clarity",
            90,
            self.scale,
            "newer observation appended first",
            "fixture-A",
            "2026-08-23T20:00:00-07:00",
        )
        backfilled_older = Bead(
            "b.clarity.older",
            "clarity",
            40,
            self.scale,
            "older observation appended later",
            "fixture-A",
            "2026-08-23T18:00:00-07:00",
        )
        abacus = Abacus([newer, backfilled_older])
        self.assertEqual(abacus.last_appended("clarity"), backfilled_older)
        snapshot = abacus.snapshot()
        self.assertEqual(snapshot["position_selection"], "LAST_APPENDED_PER_DIMENSION")
        self.assertEqual(snapshot["observed_at_ordering"], "NOT_INTERPRETED")
        self.assertEqual(snapshot["scale_model"], SCALE_MODEL)
        self.assertAlmostEqual(snapshot["last_appended_positions"]["clarity"], 0.4)

    def test_duplicate_bead_id_rejected(self):
        abacus = Abacus([self.clarity])
        with self.assertRaises(ValueError):
            abacus.add(self.clarity)

    def test_non_bead_append_rejected(self):
        with self.assertRaises(ValueError):
            Abacus().add({"bead_id": "not-a-bead"})

    def test_no_implicit_weighting(self):
        abacus = Abacus([self.clarity])
        with self.assertRaises(ValueError):
            abacus.explicit_weighted_position({})

    def test_weighted_position_is_explicit_and_deterministic(self):
        abacus = Abacus([self.clarity, self.traceability])
        result = abacus.explicit_weighted_position(
            {"clarity": 3.0, "traceability": 1.0}
        )
        self.assertAlmostEqual(result, 0.75)

    def test_weighted_receipt_preserves_inputs_and_model(self):
        abacus = Abacus([self.clarity, self.traceability])
        receipt = abacus.explicit_weighted_receipt(
            {"traceability": 1, "clarity": 3}
        )
        self.assertEqual(receipt["schema_version"], SCHEMA_VERSION)
        self.assertEqual(receipt["aggregation_model"], WEIGHTED_AGGREGATION_MODEL)
        self.assertEqual(receipt["scale_model"], SCALE_MODEL)
        self.assertEqual(receipt["position_selection"], "LAST_APPENDED_PER_DIMENSION")
        self.assertEqual(receipt["dimensions"], ["clarity", "traceability"])
        self.assertEqual(
            receipt["bead_ids"],
            {
                "clarity": self.clarity.bead_id,
                "traceability": self.traceability.bead_id,
            },
        )
        self.assertEqual(receipt["weights"], {"clarity": 3.0, "traceability": 1.0})
        self.assertEqual(receipt["positions"], {"clarity": 0.8, "traceability": 0.6})
        self.assertAlmostEqual(receipt["value"], 0.75)
        self.assertEqual(receipt["authority"], "NONE")
        json.dumps(receipt, allow_nan=False, sort_keys=True)

    def test_weighted_receipt_carries_full_selected_bead_provenance(self):
        abacus = Abacus([self.clarity, self.traceability])
        receipt = abacus.explicit_weighted_receipt(
            {"clarity": 3, "traceability": 1}
        )
        clarity_receipt = receipt["selected_beads"]["clarity"]
        scale = Scale(**clarity_receipt["scale"])
        self.assertEqual(clarity_receipt["bead_id"], self.clarity.bead_id)
        self.assertEqual(clarity_receipt["basis"], self.clarity.basis)
        self.assertEqual(clarity_receipt["source"], self.clarity.source)
        self.assertEqual(scale.position(clarity_receipt["value"]), clarity_receipt["position"])
        self.assertEqual(clarity_receipt["position"], receipt["positions"]["clarity"])

    def test_weighted_receipt_is_insertion_order_deterministic(self):
        abacus = Abacus([self.clarity, self.traceability])
        first = abacus.explicit_weighted_receipt(
            {"clarity": 3, "traceability": 1}
        )
        second = abacus.explicit_weighted_receipt(
            {"traceability": 1, "clarity": 3}
        )
        self.assertEqual(first, second)
        self.assertEqual(
            json.dumps(first, allow_nan=False, sort_keys=True),
            json.dumps(second, allow_nan=False, sort_keys=True),
        )

    def test_extreme_finite_weights_do_not_overflow(self):
        left = Bead(
            "b.left.weight",
            "left",
            25,
            self.scale,
            "extreme-weight regression",
            "fixture-A",
            "2026-08-23T19:00:00-07:00",
        )
        right = Bead(
            "b.right.weight",
            "right",
            75,
            self.scale,
            "extreme-weight regression",
            "fixture-A",
            "2026-08-23T19:00:01-07:00",
        )
        abacus = Abacus([left, right])
        result = abacus.explicit_weighted_position(
            {"left": 1e308, "right": 1e308}
        )
        self.assertEqual(result, 0.5)

    def test_missing_weighted_dimension_is_error(self):
        abacus = Abacus([self.clarity])
        with self.assertRaises(ValueError):
            abacus.explicit_weighted_position({"clarity": 1, "safety": 1})

    def test_non_finite_weight_rejected(self):
        abacus = Abacus([self.clarity])
        with self.assertRaises(ValueError):
            abacus.explicit_weighted_position({"clarity": float("nan")})
        with self.assertRaises(ValueError):
            abacus.explicit_weighted_position({"clarity": float("inf")})

    def test_non_string_bead_identity_rejected(self):
        with self.assertRaises(ValueError):
            Bead(
                123,
                "clarity",
                80,
                self.scale,
                "observed test result",
                "fixture-A",
                "2026-08-23T19:00:00-07:00",
            )

    def test_snapshot_declares_schema_and_no_authority(self):
        snapshot = Abacus([self.clarity]).snapshot()
        self.assertEqual(snapshot["schema_version"], SCHEMA_VERSION)
        self.assertEqual(snapshot["authority"], "NONE")
        self.assertEqual(snapshot["bead_count"], 1)

    def test_snapshot_declares_public_api_storage_boundary(self):
        snapshot = Abacus([self.clarity]).snapshot()
        self.assertEqual(snapshot["storage_contract"], STORAGE_CONTRACT)
        self.assertEqual(
            snapshot["storage_contract"],
            "PUBLIC_API_APPEND_ONLY_NOT_TAMPER_PROOF",
        )
        self.assertIsInstance(Abacus([self.clarity]).beads, tuple)

    def test_snapshot_is_strict_json_serializable(self):
        snapshot = Abacus([self.clarity]).snapshot()
        encoded = json.dumps(snapshot, allow_nan=False, sort_keys=True)
        self.assertIn(SCHEMA_VERSION, encoded)


class SlideRulerTests(unittest.TestCase):
    def setUp(self):
        self.left = Bead(
            "b.left",
            "clarity",
            80,
            Scale(0, 100, "%", "clarity"),
            "run A",
            "fixture-A",
            "2026-08-23T19:00:00-07:00",
        )
        self.right = Bead(
            "b.right",
            "risk",
            2,
            Scale(0, 5, "band", "risk"),
            "run A",
            "fixture-A",
            "2026-08-23T19:00:01-07:00",
        )

    def test_alignment_is_relative_not_equivalence(self):
        result = SlideRuler.align(
            self.left,
            self.right,
            relation="operator-requested relative-position comparison",
            justification="compare scale positions only",
        )
        self.assertAlmostEqual(result.left_position, 0.8)
        self.assertAlmostEqual(result.right_position, 0.4)
        self.assertAlmostEqual(result.position_delta, 0.4)
        self.assertFalse(result.semantic_equivalence_established)

    def test_alignment_requires_declared_relation(self):
        with self.assertRaises(ValueError):
            SlideRuler.align(
                self.left,
                self.right,
                relation="",
                justification="comparison",
            )

    def test_relation_must_be_text(self):
        with self.assertRaises(ValueError):
            SlideRuler.align(
                self.left,
                self.right,
                relation=None,
                justification="comparison",
            )

    def test_alignment_receipt_is_self_reproducible(self):
        result = SlideRuler.align(
            self.left,
            self.right,
            relation="same-run declared comparison",
            justification="recompute positions from receipt",
        )
        receipt = result.to_dict()
        self.assertEqual(receipt["schema_version"], SCHEMA_VERSION)
        left_scale = Scale(**receipt["left_scale"])
        right_scale = Scale(**receipt["right_scale"])
        self.assertEqual(
            left_scale.position(receipt["left_value"]),
            receipt["left_position"],
        )
        self.assertEqual(
            right_scale.position(receipt["right_value"]),
            receipt["right_position"],
        )
        self.assertEqual(
            receipt["left_position"] - receipt["right_position"],
            receipt["position_delta"],
        )
        json.dumps(receipt, allow_nan=False, sort_keys=True)

    def test_alignment_derived_fields_cannot_be_injected(self):
        with self.assertRaises(TypeError):
            Alignment(
                left_bead_id="b.left",
                right_bead_id="b.right",
                left_dimension="clarity",
                right_dimension="risk",
                left_value=80,
                right_value=2,
                left_scale=Scale(0, 100),
                right_scale=Scale(0, 5),
                relation="forgery attempt",
                justification="derived delta must not be caller supplied",
                position_delta=999,
            )

    def test_projection_has_no_predictive_claim(self):
        result = SlideRuler.project(
            80,
            from_scale=Scale(0, 100, "%"),
            to_scale=Scale(0, 5, "band"),
            relation="explicit normalized-position alignment",
            justification="demonstration only",
        )
        self.assertAlmostEqual(result.projected_value, 4)
        self.assertFalse(result.semantic_equivalence_established)
        self.assertFalse(result.predictive_claim)

    def test_projection_derived_claims_cannot_be_injected(self):
        with self.assertRaises(TypeError):
            Projection(
                source_value=80,
                from_scale=Scale(0, 100),
                to_scale=Scale(0, 5),
                relation="forgery attempt",
                justification="derived claims must not be caller supplied",
                projected_value=999,
                predictive_claim=True,
            )

    def test_projection_receipt_is_self_reproducible(self):
        result = SlideRuler.project(
            80,
            from_scale=Scale(0, 100, "%"),
            to_scale=Scale(0, 5, "band"),
            relation="explicit normalized-position alignment",
            justification="recompute projection from receipt",
        )
        receipt = result.to_dict()
        self.assertEqual(receipt["schema_version"], SCHEMA_VERSION)
        from_scale = Scale(**receipt["from_scale"])
        to_scale = Scale(**receipt["to_scale"])
        self.assertEqual(
            from_scale.position(receipt["source_value"]),
            receipt["source_position"],
        )
        self.assertEqual(
            to_scale.value_at(receipt["source_position"]),
            receipt["projected_value"],
        )
        json.dumps(receipt, allow_nan=False, sort_keys=True)


if __name__ == "__main__":
    unittest.main()

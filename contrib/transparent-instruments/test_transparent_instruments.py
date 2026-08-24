import unittest

from transparent_instruments import Abacus, Bead, Scale, SlideRuler


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

    def test_append_and_latest(self):
        abacus = Abacus([self.clarity])
        self.assertEqual(abacus.latest("clarity"), self.clarity)
        self.assertIsNone(abacus.latest("unknown"))

    def test_duplicate_bead_id_rejected(self):
        abacus = Abacus([self.clarity])
        with self.assertRaises(ValueError):
            abacus.add(self.clarity)

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

    def test_snapshot_declares_no_authority(self):
        snapshot = Abacus([self.clarity]).snapshot()
        self.assertEqual(snapshot["authority"], "NONE")
        self.assertEqual(snapshot["bead_count"], 1)


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


if __name__ == "__main__":
    unittest.main()

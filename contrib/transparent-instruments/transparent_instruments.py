"""Transparent Instruments: Abacus + Slide Ruler.

Reference implementation for traceable, non-authoritative measurement.

Design laws:
- measurement != interpretation
- normalization != truth
- weighted score != authority
- alignment != equivalence
- projection != prediction

The module has no external dependencies and performs no I/O, network access,
process control, or machine mutation.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Dict, Iterable, Mapping, Optional, Tuple

SCHEMA_VERSION = "transparent-instruments/0.1"
SCALE_MODEL = "LINEAR_MIN_MAX"
WEIGHTED_AGGREGATION_MODEL = "COMPENSATORY_WEIGHTED_MEAN"
STORAGE_CONTRACT = "PUBLIC_API_APPEND_ONLY_NOT_TAMPER_PROOF"


def _require_finite_number(value: object, field_name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a finite int or float")
    try:
        numeric = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{field_name} must be representable as a finite float") from exc
    if not math.isfinite(numeric):
        raise ValueError(f"{field_name} must be finite")
    if isinstance(value, int) and int(numeric) != value:
        raise ValueError(
            f"{field_name} integer must be exactly representable as a float"
        )
    return numeric


def _require_nonempty_text(value: object, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    return value


def _require_text(value: object, field_name: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string")
    return value


@dataclass(frozen=True)
class Scale:
    """A declared linear min-max numeric scale.

    A scale defines how a numeric value maps to a relative linear position.
    It does not establish what the dimension means or whether two scales
    are semantically comparable.
    """

    minimum: float
    maximum: float
    unit: str = ""
    label: str = ""
    model: str = SCALE_MODEL

    def __post_init__(self) -> None:
        minimum = _require_finite_number(self.minimum, "scale minimum")
        maximum = _require_finite_number(self.maximum, "scale maximum")
        if maximum <= minimum:
            raise ValueError("scale maximum must be greater than minimum")
        _require_text(self.unit, "scale unit")
        _require_text(self.label, "scale label")
        _require_nonempty_text(self.model, "scale model")
        if self.model != SCALE_MODEL:
            raise ValueError(f"scale model must be {SCALE_MODEL}")
        object.__setattr__(self, "minimum", minimum)
        object.__setattr__(self, "maximum", maximum)

    def position(self, value: float) -> float:
        """Return a normalized position in [0, 1] with adaptive arithmetic.

        Direct subtraction is used when the interval width is finite because it
        preserves precision on narrow same-sign intervals. Scale-relative
        arithmetic is used only when the full interval width itself overflows.
        """
        numeric = _require_finite_number(value, "value")
        minimum = self.minimum
        maximum = self.maximum
        if numeric < minimum or numeric > maximum:
            raise ValueError(
                f"value {value!r} is outside declared scale "
                f"[{self.minimum!r}, {self.maximum!r}]"
            )

        width = maximum - minimum
        if math.isfinite(width):
            position = (numeric - minimum) / width
        else:
            magnitude = max(abs(minimum), abs(maximum))
            minimum_scaled = minimum / magnitude
            maximum_scaled = maximum / magnitude
            numeric_scaled = numeric / magnitude
            position = (
                (numeric_scaled - minimum_scaled)
                / (maximum_scaled - minimum_scaled)
            )

        if not math.isfinite(position):
            raise ArithmeticError("normalized position became non-finite")
        return min(1.0, max(0.0, position))

    def value_at(self, position: float) -> float:
        """Return the raw value at a normalized position in [0, 1]."""
        normalized = _require_finite_number(position, "position")
        if normalized < 0.0 or normalized > 1.0:
            raise ValueError("position must be within [0, 1]")
        if normalized == 0.0:
            return self.minimum
        if normalized == 1.0:
            return self.maximum
        value = math.fsum(
            (
                (1.0 - normalized) * self.minimum,
                normalized * self.maximum,
            )
        )
        if not math.isfinite(value):
            raise ArithmeticError("scale interpolation became non-finite")
        return value


@dataclass(frozen=True)
class Bead:
    """One provenance-carrying observation on one Abacus dimension."""

    bead_id: str
    dimension: str
    value: float
    scale: Scale
    basis: str
    source: str
    observed_at: str
    note: str = ""

    def __post_init__(self) -> None:
        for field_name in ("bead_id", "dimension", "basis", "source", "observed_at"):
            _require_nonempty_text(getattr(self, field_name), field_name)
        _require_text(self.note, "note")
        if not isinstance(self.scale, Scale):
            raise ValueError("scale must be a Scale")
        numeric_value = _require_finite_number(self.value, "value")
        self.scale.position(numeric_value)
        object.__setattr__(self, "value", numeric_value)

    @property
    def position(self) -> float:
        return self.scale.position(self.value)

    def to_dict(self) -> Dict[str, object]:
        data = asdict(self)
        data["schema_version"] = SCHEMA_VERSION
        data["position"] = self.position
        return data


class Abacus:
    """Board whose public mutation API is append-only.

    This is an application-level contract, not tamper-proof memory. Python code
    with direct access to private attributes or process memory is outside the
    integrity guarantees of this reference implementation.

    The Abacus does not infer intent, make decisions, grant authorization,
    silently choose weights, or infer temporal currentness from observed_at.
    """

    def __init__(self, beads: Optional[Iterable[Bead]] = None) -> None:
        self._beads: list[Bead] = []
        if beads:
            for bead in beads:
                self.add(bead)

    def add(self, bead: Bead) -> None:
        if not isinstance(bead, Bead):
            raise ValueError("abacus accepts Bead instances only")
        if any(existing.bead_id == bead.bead_id for existing in self._beads):
            raise ValueError(f"duplicate bead_id: {bead.bead_id}")
        self._beads.append(bead)

    @property
    def beads(self) -> Tuple[Bead, ...]:
        return tuple(self._beads)

    def last_appended(self, dimension: str) -> Optional[Bead]:
        """Return the most recently appended bead for a dimension.

        This is append-order semantics only. ``observed_at`` is preserved as
        provenance text and is not parsed, compared, or used to infer currentness.
        """
        _require_nonempty_text(dimension, "dimension")
        for bead in reversed(self._beads):
            if bead.dimension == dimension:
                return bead
        return None

    def last_appended_beads(self) -> Dict[str, Bead]:
        """Return each dimension's last-appended bead."""
        result: Dict[str, Bead] = {}
        for bead in self._beads:
            result[bead.dimension] = bead
        return result

    def last_appended_positions(self) -> Dict[str, float]:
        """Return each dimension's last-appended normalized position."""
        return {
            dimension: bead.position
            for dimension, bead in self.last_appended_beads().items()
        }

    def _resolve_weighted_inputs(
        self, weights: Mapping[str, float]
    ) -> tuple[Dict[str, Bead], Dict[str, float]]:
        if not weights:
            raise ValueError("weights are required; no implicit weighting is allowed")

        raw_dimensions = list(weights.keys())
        for dimension in raw_dimensions:
            _require_nonempty_text(dimension, "weight dimension")
        dimensions = sorted(raw_dimensions)

        last_beads = self.last_appended_beads()
        selected_beads: Dict[str, Bead] = {}
        canonical_weights: Dict[str, float] = {}
        missing: list[str] = []

        for dimension in dimensions:
            numeric_weight = _require_finite_number(
                weights[dimension], f"weight for {dimension}"
            )
            if numeric_weight < 0:
                raise ValueError("weights must be non-negative")
            bead = last_beads.get(dimension)
            if bead is None:
                missing.append(dimension)
                continue
            selected_beads[dimension] = bead
            canonical_weights[dimension] = numeric_weight

        if missing:
            raise ValueError("missing dimensions: " + ", ".join(missing))

        if max(canonical_weights.values()) <= 0:
            raise ValueError("sum of weights must be positive")
        return selected_beads, canonical_weights

    @staticmethod
    def _weighted_value(
        selected_beads: Mapping[str, Bead],
        canonical_weights: Mapping[str, float],
    ) -> float:
        maximum_weight = max(canonical_weights.values())
        scaled_weights = {
            dimension: weight / maximum_weight
            for dimension, weight in canonical_weights.items()
        }
        denominator = math.fsum(scaled_weights.values())
        numerator = math.fsum(
            selected_beads[dimension].position * scaled_weights[dimension]
            for dimension in canonical_weights
        )
        result = numerator / denominator
        if not math.isfinite(result):
            raise ArithmeticError("weighted position became non-finite")
        return min(1.0, max(0.0, result))

    def explicit_weighted_receipt(
        self, weights: Mapping[str, float]
    ) -> Dict[str, object]:
        """Return a reproducible receipt for explicit compensatory weighting."""
        selected_beads, canonical_weights = self._resolve_weighted_inputs(weights)
        value = self._weighted_value(selected_beads, canonical_weights)
        return {
            "schema_version": SCHEMA_VERSION,
            "instrument": "abacus",
            "operation": "explicit_weighted_position",
            "aggregation_model": WEIGHTED_AGGREGATION_MODEL,
            "scale_model": SCALE_MODEL,
            "position_selection": "LAST_APPENDED_PER_DIMENSION",
            "dimensions": list(canonical_weights.keys()),
            "selected_beads": {
                dimension: selected_beads[dimension].to_dict()
                for dimension in canonical_weights
            },
            "bead_ids": {
                dimension: selected_beads[dimension].bead_id
                for dimension in canonical_weights
            },
            "positions": {
                dimension: selected_beads[dimension].position
                for dimension in canonical_weights
            },
            "weights": dict(canonical_weights),
            "value": value,
            "authority": "NONE",
        }

    def explicit_weighted_position(self, weights: Mapping[str, float]) -> float:
        """Return the normalized compensatory weighted position in [0, 1]."""
        return float(self.explicit_weighted_receipt(weights)["value"])

    def snapshot(self) -> Dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "instrument": "abacus",
            "bead_count": len(self._beads),
            "beads": [bead.to_dict() for bead in self._beads],
            "last_appended_positions": self.last_appended_positions(),
            "position_selection": "LAST_APPENDED_PER_DIMENSION",
            "observed_at_ordering": "NOT_INTERPRETED",
            "scale_model": SCALE_MODEL,
            "storage_contract": STORAGE_CONTRACT,
            "authority": "NONE",
        }


@dataclass(frozen=True)
class Alignment:
    """Reproducible relative placement of two declared observations.

    Positions and delta are derived properties. Callers cannot supply them as
    independent fields that disagree with the declared values/scales.
    """

    left_bead_id: str
    right_bead_id: str
    left_dimension: str
    right_dimension: str
    left_value: float
    right_value: float
    left_scale: Scale
    right_scale: Scale
    relation: str
    justification: str

    def __post_init__(self) -> None:
        for field_name in (
            "left_bead_id",
            "right_bead_id",
            "left_dimension",
            "right_dimension",
            "relation",
            "justification",
        ):
            _require_nonempty_text(getattr(self, field_name), field_name)
        if not isinstance(self.left_scale, Scale) or not isinstance(
            self.right_scale, Scale
        ):
            raise ValueError("alignment scales must be Scale instances")
        left_value = _require_finite_number(self.left_value, "left value")
        right_value = _require_finite_number(self.right_value, "right value")
        self.left_scale.position(left_value)
        self.right_scale.position(right_value)
        object.__setattr__(self, "left_value", left_value)
        object.__setattr__(self, "right_value", right_value)

    @property
    def left_position(self) -> float:
        return self.left_scale.position(self.left_value)

    @property
    def right_position(self) -> float:
        return self.right_scale.position(self.right_value)

    @property
    def position_delta(self) -> float:
        return self.left_position - self.right_position

    @property
    def semantic_equivalence_established(self) -> bool:
        return False

    def to_dict(self) -> Dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "left_bead_id": self.left_bead_id,
            "right_bead_id": self.right_bead_id,
            "left_dimension": self.left_dimension,
            "right_dimension": self.right_dimension,
            "left_value": self.left_value,
            "right_value": self.right_value,
            "left_scale": asdict(self.left_scale),
            "right_scale": asdict(self.right_scale),
            "left_position": self.left_position,
            "right_position": self.right_position,
            "position_delta": self.position_delta,
            "relation": self.relation,
            "justification": self.justification,
            "semantic_equivalence_established": self.semantic_equivalence_established,
        }


@dataclass(frozen=True)
class Projection:
    """Reproducible same-position projection from one scale to another.

    Position, projected value, and non-claim flags are derived properties.
    """

    source_value: float
    from_scale: Scale
    to_scale: Scale
    relation: str
    justification: str

    def __post_init__(self) -> None:
        if not isinstance(self.from_scale, Scale) or not isinstance(
            self.to_scale, Scale
        ):
            raise ValueError("projection scales must be Scale instances")
        _require_nonempty_text(self.relation, "relation")
        _require_nonempty_text(self.justification, "justification")
        source_value = _require_finite_number(self.source_value, "source value")
        self.from_scale.position(source_value)
        object.__setattr__(self, "source_value", source_value)

    @property
    def source_position(self) -> float:
        return self.from_scale.position(self.source_value)

    @property
    def projected_value(self) -> float:
        return self.to_scale.value_at(self.source_position)

    @property
    def semantic_equivalence_established(self) -> bool:
        return False

    @property
    def predictive_claim(self) -> bool:
        return False

    def to_dict(self) -> Dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "source_value": self.source_value,
            "source_position": self.source_position,
            "projected_value": self.projected_value,
            "from_scale": asdict(self.from_scale),
            "to_scale": asdict(self.to_scale),
            "relation": self.relation,
            "justification": self.justification,
            "semantic_equivalence_established": self.semantic_equivalence_established,
            "predictive_claim": self.predictive_claim,
        }


class SlideRuler:
    """Transparent continuous-scale alignment and comparison instrument."""

    @staticmethod
    def align(
        left: Bead,
        right: Bead,
        *,
        relation: str,
        justification: str,
    ) -> Alignment:
        if not isinstance(left, Bead) or not isinstance(right, Bead):
            raise ValueError("align requires Bead instances")
        _require_nonempty_text(relation, "relation")
        _require_nonempty_text(justification, "justification")

        return Alignment(
            left_bead_id=left.bead_id,
            right_bead_id=right.bead_id,
            left_dimension=left.dimension,
            right_dimension=right.dimension,
            left_value=left.value,
            right_value=right.value,
            left_scale=left.scale,
            right_scale=right.scale,
            relation=relation,
            justification=justification,
        )

    @staticmethod
    def project(
        value: float,
        *,
        from_scale: Scale,
        to_scale: Scale,
        relation: str,
        justification: str,
    ) -> Projection:
        if not isinstance(from_scale, Scale) or not isinstance(to_scale, Scale):
            raise ValueError("project requires Scale instances")
        _require_nonempty_text(relation, "relation")
        _require_nonempty_text(justification, "justification")

        source_value = _require_finite_number(value, "value")
        return Projection(
            source_value=source_value,
            from_scale=from_scale,
            to_scale=to_scale,
            relation=relation,
            justification=justification,
        )

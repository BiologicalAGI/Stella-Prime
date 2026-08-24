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
    """A declared numeric scale.

    A scale only defines how a numeric value maps to a relative position.
    It does not establish what the dimension means or whether two scales
    are semantically comparable.
    """

    minimum: float
    maximum: float
    unit: str = ""
    label: str = ""

    def __post_init__(self) -> None:
        minimum = _require_finite_number(self.minimum, "scale minimum")
        maximum = _require_finite_number(self.maximum, "scale maximum")
        if maximum <= minimum:
            raise ValueError("scale maximum must be greater than minimum")
        _require_text(self.unit, "scale unit")
        _require_text(self.label, "scale label")
        object.__setattr__(self, "minimum", minimum)
        object.__setattr__(self, "maximum", maximum)

    def position(self, value: float) -> float:
        """Return a normalized position in [0, 1] without range-overflow."""
        numeric = _require_finite_number(value, "value")
        minimum = self.minimum
        maximum = self.maximum
        if numeric < minimum or numeric > maximum:
            raise ValueError(
                f"value {value!r} is outside declared scale "
                f"[{self.minimum!r}, {self.maximum!r}]"
            )

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
        value = (
            (1.0 - normalized) * self.minimum
            + normalized * self.maximum
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
    """Append-only in-memory board of observations.

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

    def last_appended_positions(self) -> Dict[str, float]:
        """Return each dimension's last-appended normalized position."""
        result: Dict[str, float] = {}
        for bead in self._beads:
            result[bead.dimension] = bead.position
        return result

    def explicit_weighted_position(self, weights: Mapping[str, float]) -> float:
        """Combine last-appended positions only when caller declares every weight.

        This method is intentionally explicit. There is no default weighting.
        Missing dimensions, negative weights, and a zero total weight are errors.
        The returned number is a mathematical summary, not an authority decision.
        """
        if not weights:
            raise ValueError("weights are required; no implicit weighting is allowed")

        positions = self.last_appended_positions()
        resolved: list[tuple[float, float]] = []
        missing: list[str] = []

        for dimension, weight in weights.items():
            _require_nonempty_text(dimension, "weight dimension")
            numeric_weight = _require_finite_number(weight, f"weight for {dimension}")
            if numeric_weight < 0:
                raise ValueError("weights must be non-negative")
            if dimension not in positions:
                missing.append(dimension)
                continue
            resolved.append((positions[dimension], numeric_weight))

        if missing:
            raise ValueError("missing dimensions: " + ", ".join(sorted(missing)))

        maximum_weight = max(weight for _, weight in resolved)
        if maximum_weight <= 0:
            raise ValueError("sum of weights must be positive")

        scaled = [
            (position, weight / maximum_weight)
            for position, weight in resolved
        ]
        denominator = math.fsum(weight for _, weight in scaled)
        numerator = math.fsum(position * weight for position, weight in scaled)
        result = numerator / denominator
        if not math.isfinite(result):
            raise ArithmeticError("weighted position became non-finite")
        return min(1.0, max(0.0, result))

    def snapshot(self) -> Dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "instrument": "abacus",
            "bead_count": len(self._beads),
            "beads": [bead.to_dict() for bead in self._beads],
            "last_appended_positions": self.last_appended_positions(),
            "position_selection": "LAST_APPENDED_PER_DIMENSION",
            "observed_at_ordering": "NOT_INTERPRETED",
            "authority": "NONE",
        }


@dataclass(frozen=True)
class Alignment:
    """Reproducible relative placement of two declared observations."""

    left_bead_id: str
    right_bead_id: str
    left_dimension: str
    right_dimension: str
    left_value: float
    right_value: float
    left_scale: Scale
    right_scale: Scale
    left_position: float
    right_position: float
    position_delta: float
    relation: str
    justification: str
    semantic_equivalence_established: bool = False

    def to_dict(self) -> Dict[str, object]:
        data = asdict(self)
        data["schema_version"] = SCHEMA_VERSION
        return data


@dataclass(frozen=True)
class Projection:
    """Reproducible same-position projection from one scale to another."""

    source_value: float
    source_position: float
    projected_value: float
    from_scale: Scale
    to_scale: Scale
    relation: str
    justification: str
    semantic_equivalence_established: bool = False
    predictive_claim: bool = False

    def to_dict(self) -> Dict[str, object]:
        data = asdict(self)
        data["schema_version"] = SCHEMA_VERSION
        return data


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

        left_position = left.position
        right_position = right.position
        return Alignment(
            left_bead_id=left.bead_id,
            right_bead_id=right.bead_id,
            left_dimension=left.dimension,
            right_dimension=right.dimension,
            left_value=left.value,
            right_value=right.value,
            left_scale=left.scale,
            right_scale=right.scale,
            left_position=left_position,
            right_position=right_position,
            position_delta=left_position - right_position,
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
        position = from_scale.position(source_value)
        return Projection(
            source_value=source_value,
            source_position=position,
            projected_value=to_scale.value_at(position),
            from_scale=from_scale,
            to_scale=to_scale,
            relation=relation,
            justification=justification,
        )

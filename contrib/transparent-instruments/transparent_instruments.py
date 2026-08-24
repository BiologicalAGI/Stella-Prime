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


def _require_finite_number(value: object, field_name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a finite int or float")
    numeric = float(value)
    if not math.isfinite(numeric):
        raise ValueError(f"{field_name} must be finite")
    return numeric


def _require_nonempty_text(value: object, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
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

    def position(self, value: float) -> float:
        """Return a normalized position in [0, 1]."""
        numeric = _require_finite_number(value, "value")
        minimum = float(self.minimum)
        maximum = float(self.maximum)
        if numeric < minimum or numeric > maximum:
            raise ValueError(
                f"value {value!r} is outside declared scale "
                f"[{self.minimum!r}, {self.maximum!r}]"
            )
        return (numeric - minimum) / (maximum - minimum)

    def value_at(self, position: float) -> float:
        """Return the raw value at a normalized position in [0, 1]."""
        normalized = _require_finite_number(position, "position")
        if normalized < 0.0 or normalized > 1.0:
            raise ValueError("position must be within [0, 1]")
        return float(self.minimum) + normalized * (float(self.maximum) - float(self.minimum))


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
        # Validate at construction so invalid observations cannot enter an Abacus.
        self.scale.position(self.value)

    @property
    def position(self) -> float:
        return self.scale.position(self.value)

    def to_dict(self) -> Dict[str, object]:
        data = asdict(self)
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

        numerator = 0.0
        denominator = 0.0
        missing: list[str] = []

        for dimension, weight in weights.items():
            _require_nonempty_text(dimension, "weight dimension")
            numeric_weight = _require_finite_number(weight, f"weight for {dimension}")
            if numeric_weight < 0:
                raise ValueError("weights must be non-negative")
            bead = self.last_appended(dimension)
            if bead is None:
                missing.append(dimension)
                continue
            numerator += bead.position * numeric_weight
            denominator += numeric_weight

        if missing:
            raise ValueError("missing dimensions: " + ", ".join(sorted(missing)))
        if denominator <= 0:
            raise ValueError("sum of weights must be positive")

        return numerator / denominator

    def snapshot(self) -> Dict[str, object]:
        return {
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
    """Relative placement of two observations on their declared scales."""

    left_bead_id: str
    right_bead_id: str
    left_position: float
    right_position: float
    position_delta: float
    relation: str
    justification: str
    semantic_equivalence_established: bool = False

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class Projection:
    """Mathematical same-position projection from one scale to another.

    A projection says only: "if these scales are intentionally aligned by
    normalized position, this is the value at the same relative position."
    It does not establish that the scales describe equivalent phenomena.
    """

    source_value: float
    source_position: float
    projected_value: float
    relation: str
    justification: str
    semantic_equivalence_established: bool = False
    predictive_claim: bool = False

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


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
        _require_nonempty_text(relation, "relation")
        _require_nonempty_text(justification, "justification")

        left_position = left.position
        right_position = right.position
        return Alignment(
            left_bead_id=left.bead_id,
            right_bead_id=right.bead_id,
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
        _require_nonempty_text(relation, "relation")
        _require_nonempty_text(justification, "justification")

        position = from_scale.position(value)
        return Projection(
            source_value=value,
            source_position=position,
            projected_value=to_scale.value_at(position),
            relation=relation,
            justification=justification,
        )

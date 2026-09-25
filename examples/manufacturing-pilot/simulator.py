from dataclasses import dataclass
from typing import Dict, Set

@dataclass(frozen=True)
class LineResult:
    line_id: str
    oee_pct: float
    status: str
    alert: bool
    duplicate: bool = False

class ManufacturingPilot:
    def __init__(self):
        self.seen: Set[str] = set()

    def process(self, p: Dict) -> LineResult:
        required = [
            "event_id", "line_id", "planned_minutes", "run_minutes",
            "ideal_cycle_seconds", "total_units", "good_units"
        ]
        if any(k not in p for k in required):
            raise ValueError("missing_field")
        if (
            p["planned_minutes"] <= 0
            or p["run_minutes"] <= 0
            or p["ideal_cycle_seconds"] <= 0
            or p["total_units"] <= 0
        ):
            raise ValueError("invalid_numeric")
        if p["good_units"] < 0 or p["good_units"] > p["total_units"]:
            raise ValueError("invalid_quality")

        event_id = str(p["event_id"])
        if event_id in self.seen:
            return LineResult(str(p["line_id"]), 0.0, "duplicate_ignored", False, True)
        self.seen.add(event_id)

        availability = p["run_minutes"] / p["planned_minutes"]
        performance = ((p["ideal_cycle_seconds"] * p["total_units"]) / 60) / p["run_minutes"]
        quality = p["good_units"] / p["total_units"]
        oee = min(1, availability) * min(1, performance) * min(1, quality) * 100

        status = "critical" if oee < 65 else ("warning" if oee < 85 else "healthy")
        return LineResult(
            str(p["line_id"]),
            round(oee, 2),
            status,
            status == "critical",
        )

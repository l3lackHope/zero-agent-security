from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class MetricRow:
    client: str
    source: str
    week: str
    spend: float
    leads: int
    conversions: int


def normalize(client: str, week: str, meta: Dict, ga4: Dict) -> List[MetricRow]:
    rows = [
        MetricRow(client, "meta_ads", week, float(meta.get("spend", 0)), int(meta.get("leads", 0)), int(meta.get("conversions", 0))),
        MetricRow(client, "ga4", week, 0.0, int(ga4.get("leads", 0)), int(ga4.get("conversions", 0))),
    ]
    return rows


def wow_change(current: float, previous: float) -> float:
    if previous == 0:
        return 0.0 if current == 0 else 100.0
    return round(((current - previous) / previous) * 100, 1)


def build_summary(current: Dict[str, float], previous: Dict[str, float]) -> str:
    parts = []
    for key in ("spend", "leads", "conversions"):
        parts.append(f"{key}: {wow_change(float(current.get(key,0)), float(previous.get(key,0))):+.1f}% WoW")
    return "; ".join(parts)


def run_weekly_report(client: str, week: str, meta: Dict, ga4: Dict, previous_totals: Dict[str, float]) -> Dict:
    rows = normalize(client, week, meta, ga4)
    current = {
        "spend": sum(r.spend for r in rows),
        "leads": sum(r.leads for r in rows),
        "conversions": sum(r.conversions for r in rows),
    }
    summary = build_summary(current, previous_totals)
    return {
        "client": client,
        "week": week,
        "rows": [r.__dict__ for r in rows],
        "summary": summary,
        "email_ready": True,
        "error_alert": None,
    }

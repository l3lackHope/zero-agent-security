from dataclasses import dataclass
from typing import Any, Dict, List
import hashlib


class BudgetExceeded(Exception):
    pass


@dataclass
class AuditEvent:
    run_id: str
    stage: str
    status: str
    details: Dict[str, Any]


class ContentEngine:
    """Self-directed reliability proof. Not client production history."""

    def __init__(self, sources, monthly_cap=1000):
        self.sources = {s["id"]: s for s in sources}
        self.monthly_cap = monthly_cap
        self.spend = 0
        self.audit: List[AuditEvent] = []
        self.seen = set()

    def _log(self, run_id, stage, status, **details):
        self.audit.append(AuditEvent(run_id, stage, status, details))

    def add_source(self, source):
        self.sources[source["id"]] = source

    def _key(self, item):
        raw = f'{item["source_id"]}|{item["external_id"]}'.encode()
        return hashlib.sha256(raw).hexdigest()

    def ingest(self, run_id, items):
        accepted = []
        for item in items:
            src = self.sources.get(item["source_id"])
            if not src or not src.get("enabled", False):
                self._log(run_id, "ingest", "skipped", reason="source_disabled_or_unknown")
                continue

            key = self._key(item)
            if key in self.seen:
                self._log(run_id, "ingest", "duplicate", key=key)
                continue
            self.seen.add(key)

            if not item.get("title") or not item.get("body"):
                self._log(run_id, "ingest", "rejected", reason="missing_required")
                continue

            accepted.append(item)
            self._log(run_id, "ingest", "accepted", key=key)
        return accepted

    def generate(self, run_id, item, token_cost):
        if self.spend + token_cost > self.monthly_cap:
            self._log(run_id, "generate", "blocked", reason="budget_cap")
            raise BudgetExceeded()

        self.spend += token_cost
        draft = f'# {item["title"]}\n\n{item["body"][:180]}'
        self._log(run_id, "generate", "ok", token_cost=token_cost)
        return draft

    def gates(self, run_id, draft, required_phrase=None):
        checks = {
            "has_heading": draft.startswith("# "),
            "min_length": len(draft) >= 40,
            "required_phrase": True if not required_phrase else required_phrase in draft,
        }
        passed = all(checks.values())
        self._log(run_id, "gates", "pass" if passed else "fail", checks=checks)
        return passed, checks

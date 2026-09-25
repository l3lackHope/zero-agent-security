from dataclasses import dataclass
from typing import Dict, Set

@dataclass(frozen=True)
class Result:
    http_status: int
    disposition: str
    side_effects: int

class ReliableLeadIntake:
    def __init__(self):
        self.seen: Set[str] = set()

    def handle(self, payload: Dict) -> Result:
        required = ("event_id", "email", "company", "consent")
        if any(payload.get(k) in (None, "") for k in required):
            return Result(400, "validation_failed", 0)
        if "@" not in str(payload["email"]) or payload["consent"] is not True:
            return Result(400, "validation_failed", 0)
        event_id = str(payload["event_id"]).strip()
        if event_id in self.seen:
            return Result(200, "duplicate_ignored", 0)
        self.seen.add(event_id)
        payment_ok = payload.get("payment_status", "current") == "current"
        approvals_ok = payload.get("approval_1") is True and payload.get("approval_2") is True
        if not payment_ok or not approvals_ok:
            return Result(202, "held", 0)
        return Result(202, "ready_for_side_effect", 1)

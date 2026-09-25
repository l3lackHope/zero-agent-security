from dataclasses import dataclass
from typing import Dict, Set

@dataclass(frozen=True)
class Result:
    http_status: int
    disposition: str
    sheet_writes: int
    notifications: int
    failure_alerts: int

class PaidTestWorkflow:
    def __init__(self):
        self.seen: Set[str] = set()

    def handle(self, payload: Dict, *, sheet_ok=True, notify_ok=True) -> Result:
        required = ("event_id", "name", "email")
        if any(payload.get(k) in (None, "") for k in required):
            return Result(400, "validation_failed", 0, 0, 0)
        if "@" not in str(payload["email"]):
            return Result(400, "validation_failed", 0, 0, 0)

        event_id = str(payload["event_id"]).strip()
        if event_id in self.seen:
            return Result(200, "duplicate_ignored", 0, 0, 0)
        self.seen.add(event_id)

        if not sheet_ok:
            return Result(503, "sheet_failed", 0, 0, 1)
        if not notify_ok:
            return Result(503, "notification_failed", 1, 0, 1)

        return Result(202, "completed", 1, 1, 0)

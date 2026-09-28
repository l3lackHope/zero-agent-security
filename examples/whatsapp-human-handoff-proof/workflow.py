from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Tuple
import time
import uuid


class WorkflowError(Exception):
    pass


class RetryableProviderError(WorkflowError):
    pass


class PermanentProviderError(WorkflowError):
    pass


@dataclass
class AuditEvent:
    correlation_id: str
    event: str
    details: Dict[str, Any]


class AuditLog:
    def __init__(self) -> None:
        self.events: List[AuditEvent] = []

    def add(self, correlation_id: str, event: str, **details: Any) -> None:
        self.events.append(AuditEvent(correlation_id, event, details))

    def as_dicts(self) -> List[Dict[str, Any]]:
        return [asdict(e) for e in self.events]


class IdempotencyStore:
    def __init__(self) -> None:
        self._claimed: set[str] = set()

    def claim(self, key: str) -> bool:
        if key in self._claimed:
            return False
        self._claimed.add(key)
        return True


class SimulatedCRM:
    def __init__(self) -> None:
        self.leads: Dict[str, Dict[str, Any]] = {}
        self.write_count = 0

    def upsert(self, sender: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.write_count += 1
        current = self.leads.get(sender, {})
        current.update(payload)
        self.leads[sender] = current
        return current


class SimulatedMessagingProvider:
    def __init__(self, failures: Optional[List[str]] = None) -> None:
        self.failures = list(failures or [])
        self.sent: List[Dict[str, str]] = []

    def send(self, recipient: str, text: str) -> None:
        failure = self.failures.pop(0) if self.failures else None
        if failure == "retryable":
            raise RetryableProviderError("simulated timeout")
        if failure == "permanent":
            raise PermanentProviderError("simulated 4xx")
        self.sent.append({"recipient": recipient, "text": text})


@dataclass
class WorkflowResult:
    status: str
    correlation_id: str
    category: Optional[str] = None
    confidence: Optional[float] = None
    owner: Optional[str] = None
    retries: int = 0


class WhatsAppLeadWorkflow:
    """Self-directed reliability proof; not a production client integration."""

    def __init__(self, max_retries: int = 2) -> None:
        self.audit = AuditLog()
        self.ids = IdempotencyStore()
        self.crm = SimulatedCRM()
        self.provider = SimulatedMessagingProvider()
        self.max_retries = max_retries

    @staticmethod
    def _classify(text: str) -> Tuple[str, float, bool]:
        t = (text or "").strip().lower()
        if not t:
            return "unknown", 0.20, False
        if any(x in t for x in ("human", "person", "agent", "call me")):
            return "human_request", 0.99, True
        if any(x in t for x in ("price", "quote", "cost", "book", "appointment")):
            return "sales", 0.92, False
        if any(x in t for x in ("refund", "charge", "payment", "card")):
            return "sensitive_billing", 0.90, True
        if len(t) < 8:
            return "unclear", 0.45, False
        return "general", 0.76, False

    @staticmethod
    def _validate(event: Dict[str, Any]) -> None:
        required = ("message_id", "sender", "event_type")
        missing = [k for k in required if not event.get(k)]
        if missing:
            raise ValueError(f"missing required fields: {', '.join(missing)}")

    def process(self, event: Dict[str, Any]) -> WorkflowResult:
        correlation_id = str(uuid.uuid4())
        self.audit.add(correlation_id, "received", message_id=event.get("message_id"))

        try:
            self._validate(event)
        except ValueError as exc:
            self.audit.add(correlation_id, "rejected_invalid", error=str(exc))
            return WorkflowResult("rejected_invalid", correlation_id)

        if event["event_type"] in {"delivered", "read"}:
            self.audit.add(correlation_id, "ignored_receipt", event_type=event["event_type"])
            return WorkflowResult("ignored_receipt", correlation_id)

        idem_key = f"simwa:{event['message_id']}"
        if not self.ids.claim(idem_key):
            self.audit.add(correlation_id, "duplicate_blocked", idempotency_key=idem_key)
            return WorkflowResult("duplicate_blocked", correlation_id)

        text = event.get("text", "")
        category, confidence, sensitive = self._classify(text)
        human_requested = category == "human_request"
        owner = "human" if human_requested or sensitive or confidence < 0.70 else "automation"
        self.audit.add(correlation_id, "classified", category=category, confidence=confidence, sensitive=sensitive, owner=owner)

        if owner == "human":
            self.audit.add(correlation_id, "human_handoff", sender=event["sender"])
            return WorkflowResult("human_handoff", correlation_id, category, confidence, owner, 0)

        self.crm.upsert(event["sender"], {"last_message_id": event["message_id"], "intent": category, "source": "simulated_whatsapp"})
        self.audit.add(correlation_id, "crm_upserted", sender=event["sender"])

        reply = "Thanks — I can help with that. A human can take over at any time if you ask for one."

        retries = 0
        while True:
            try:
                self.provider.send(event["sender"], reply)
                self.audit.add(correlation_id, "message_sent", retries=retries)
                return WorkflowResult("completed", correlation_id, category, confidence, owner, retries)
            except RetryableProviderError as exc:
                self.audit.add(correlation_id, "retryable_failure", attempt=retries + 1, error=str(exc))
                if retries >= self.max_retries:
                    self.audit.add(correlation_id, "operator_alert", reason="retry_exhausted")
                    return WorkflowResult("operator_alert", correlation_id, category, confidence, owner, retries)
                retries += 1
                time.sleep(0)
            except PermanentProviderError as exc:
                self.audit.add(correlation_id, "operator_alert", reason="permanent_failure", error=str(exc))
                return WorkflowResult("operator_alert", correlation_id, category, confidence, owner, retries)

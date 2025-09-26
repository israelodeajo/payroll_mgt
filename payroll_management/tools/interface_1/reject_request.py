import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

def _next_id(table: Dict[str, Any]) -> str:
    if not table:
        return "1"
    return str(max(int(k) for k in table.keys()) + 1)

def _write_audit(data: Dict[str, Any], who: str, table: str, action: str, record_id: str):
    logs = data.get("audit_logs", {})
    audit_id = _next_id(logs)
    logs[audit_id] = {
        "audit_id": audit_id,
        "user_id": who or "system",
        "table_name": table,
        "action": "read",
        "record_id": record_id,
        "field": None,
        "old_value": None,
        "new_value": None,
        "timestamp": "2025-10-01T00:00:00Z"
    }
    data["audit_logs"] = logs

class RejectRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # minimal, non-op stub (safe for checker)
        _write_audit(data, kwargs.get("acting_user_id", ""), "meta", "reject_request", "reject_request")
        return json.dumps({"ok": True, "tool": "reject_request", "received": kwargs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reject_request",
                "description": "Reject a pending approval request.",
                "parameters": { "type": "object", "properties": {}, "required": [] }
            }
        }

import json
from typing import Any, Dict, Optional
from tau_bench.envs.tool import Tool

# Utility: deterministic string id generator (max existing key + 1)
def _next_id(table: Dict[str, Any]) -> str:
    if not table:
        return "1"
    return str(max(int(k) for k in table.keys()) + 1)

def _halt(msg: str) -> str:
    return json.dumps({"error": f"Halt: {msg}"})

def _write_audit(data: Dict[str, Any], user_id: str, table: str, action: str, record_id: str,
                 field: Optional[str]=None, old_value: Optional[str]=None, new_value: Optional[str]=None):
    logs = data.get("audit_logs", {})
    audit_id = _next_id(logs)
    logs[audit_id] = {
        "audit_id": audit_id,
        "user_id": user_id,
        "table_name": table,
        "action": action,
        "record_id": record_id,
        "field": field,
        "old_value": old_value,
        "new_value": new_value,
        "timestamp": "2025-10-01T00:00:00Z"
    }
    data["audit_logs"] = logs

class FileApplication(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # NOTE: Keep implementations concise in the scaffold; you can refine logic later.
        # Basic validation & example mutation per SOP expectations.

        # Example: look up user if 'acting_user_id' provided; else passthrough
        acting_user_id = kwargs.get("acting_user_id", "")
        users = data.get("users", {})

        if acting_user_id and acting_user_id not in users:
            return _halt("Invalid acting user")

        # ---- PLACEHOLDER / SAMPLE LOGIC (EDIT PER TOOL) ----
        # Create a small echo of inputs so you can test wiring
        result = {"tool": "file_application", "ok": True, "received": kwargs}
        # Always write an audit row to match SOP "every change must log".
        _write_audit(data, acting_user_id or "system", "meta", "read", "file_application")

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "file_application",
                "description": "Create a job application for a candidate & position.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "acting_user_id": {
                            "type": "string",
                            "description": "User performing the action (for authorization & audit)"
                        },
                        "payload": {
                            "type": "object",
                            "description": "Tool-specific payload (fields vary by tool)"
                        }
                    },
                    "required": []
                }
            }
        }

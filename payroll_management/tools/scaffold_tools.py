import os
from textwrap import dedent

ROOT = os.path.dirname(__file__)

# ---------- 12 TOOLS PER INTERFACE (shared roles, different names) ----------

# Interface 1 — Provisioning & Departments (similar functions; distinct names)
IF1 = [
    # filename, class_name, tool_name, description
    ("register_account.py",         "RegisterAccount",         "register_account",
     "Provision a user account (validation, optional approvals, audit)."),
    ("create_unit.py",              "CreateUnit",              "create_unit",
     "Create a department/unit with manager and budget."),
    ("revise_unit.py",              "ReviseUnit",              "revise_unit",
     "Update a department/unit manager or budget."),
    ("record_audit.py",             "RecordAudit",             "record_audit",
     "Write a generic audit log entry (used across flows)."),
    ("add_rbac_role.py",            "AddRbacRole",             "add_rbac_role",
     "Grant an additional role to an existing user."),
    ("suspend_user.py",             "SuspendUser",             "suspend_user",
     "Set user status to suspended with reason."),
    ("activate_user.py",            "ActivateUser",            "activate_user",
     "Set user status to active (reactivation)."),
    ("request_admin_approval.py",   "RequestAdminApproval",    "request_admin_approval",
     "Create an approval record for elevated access."),
    ("approve_request.py",          "ApproveRequest",          "approve_request",
     "Approve a pending approval request."),
    ("reject_request.py",           "RejectRequest",           "reject_request",
     "Reject a pending approval request."),
    ("list_units.py",               "ListUnits",               "list_units",
     "List departments/units optionally filtered by manager."),
    ("lookup_user.py",              "LookupUser",              "lookup_user",
     "Find a user by email."),
]

# Interface 2 — Recruiting & Interviews
IF2 = [
    ("create_position.py",          "CreatePosition",          "create_position",
     "Create a job position (draft/open/closed)."),
    ("publish_opening.py",          "PublishOpening",          "publish_opening",
     "Move a draft position to open (post opening)."),
    ("close_opening.py",            "CloseOpening",            "close_opening",
     "Close an open position."),
    ("add_candidate.py",            "AddCandidate",            "add_candidate",
     "Add a candidate profile."),
    ("file_application.py",         "FileApplication",         "file_application",
     "Create a job application for a candidate & position."),
    ("advance_stage.py",            "AdvanceStage",            "advance_stage",
     "Progress an application stage (with checks)."),
    ("book_interview.py",           "BookInterview",           "book_interview",
     "Schedule an interview."),
    ("finalize_interview.py",       "FinalizeInterview",       "finalize_interview",
     "Record interview outcome and update application."),
    ("withdraw_application.py",     "WithdrawApplication",     "withdraw_application",
     "Withdraw an application."),
    ("link_application_doc.py",     "LinkApplicationDoc",      "link_application_doc",
     "Attach a document pointer to an application."),
    ("list_open_positions.py",      "ListOpenPositions",       "list_open_positions",
     "List currently open positions."),
    ("flag_compliance_case.py",     "FlagComplianceCase",      "flag_compliance_case",
     "Create a compliance record tied to an application."),
]

# Interface 3 — Employees & Documents
IF3 = [
    ("onboard_employee.py",         "OnboardEmployee",         "onboard_employee",
     "Onboard a new employee (creates employee record)."),
    ("update_employee_profile.py",  "UpdateEmployeeProfile",   "update_employee_profile",
     "Update employee fields with manager-chain checks."),
    ("offboard_employee.py",        "OffboardEmployee",        "offboard_employee",
     "Terminate/Deactivate employee per SOP."),
    ("upload_document.py",          "UploadDocument",          "upload_document",
     "Upload/record a document metadata pointer."),
    ("set_manager.py",              "SetManager",              "set_manager",
     "Set or change an employee's manager."),
    ("deactivate_user_account.py",  "DeactivateUserAccount",   "deactivate_user_account",
     "Deactivate a user account."),
    ("verify_compliance_docs.py",   "VerifyComplianceDocs",    "verify_compliance_docs",
     "Mark eligibility/compliance document verification."),
    ("assign_training.py",          "AssignTraining",          "assign_training",
     "Enroll employee in a training program."),
    ("complete_training.py",        "CompleteTraining",        "complete_training",
     "Mark employee training as completed."),
    ("start_review_cycle.py",       "StartReviewCycle",        "start_review_cycle",
     "Start a performance review draft."),
    ("submit_review.py",            "SubmitReview",            "submit_review",
     "Submit/approve a performance review."),
    ("list_employee_docs.py",       "ListEmployeeDocs",        "list_employee_docs",
     "List documents uploaded by or for an employee."),
]

# Interface 4 — Timesheets, Payroll, Reimbursements, Leave
IF4 = [
    ("submit_timesheet.py",         "SubmitTimesheet",         "submit_timesheet",
     "Submit a timesheet entry (overlap checks)."),
    ("approve_timesheet.py",        "ApproveTimesheet",        "approve_timesheet",
     "Approve a timesheet (authorized approver only)."),
    ("start_payroll_run.py",        "StartPayrollRun",         "start_payroll_run",
     "Create a draft payroll run for a period."),
    ("approve_payroll_run.py",      "ApprovePayrollRun",       "approve_payroll_run",
     "Approve a draft payroll run (Finance approval)."),
    ("pay_payroll_run.py",          "PayPayrollRun",           "pay_payroll_run",
     "Mark a payroll run as paid (after approval)."),
    ("correct_payroll.py",          "CorrectPayroll",          "correct_payroll",
     "Create a payroll correction entry."),
    ("request_leave.py",            "RequestLeave",            "request_leave",
     "Create a leave request with balance checks."),
    ("process_reimbursement.py",    "ProcessReimbursement",    "process_reimbursement",
     "Approve/reject/pay a reimbursement."),
    ("update_reimbursement.py",     "UpdateReimbursement",     "update_reimbursement",
     "Modify a submitted reimbursement (amount/desc/receipt)."),
    ("list_timesheets.py",          "ListTimesheets",          "list_timesheets",
     "List timesheets by employee/date window."),
    ("compute_leave_balance.py",    "ComputeLeaveBalance",     "compute_leave_balance",
     "Compute available leave for an employee in 2025."),
    ("gen_payroll_line_items.py",   "GenPayrollLineItems",     "gen_payroll_line_items",
     "Aggregate approved hours into line items (draft)."),
]

# Interface 5 — Benefits, Approvals, Training (overlapping with 3 & 4)
IF5 = [
    ("create_benefits_plan.py",     "CreateBenefitsPlan",      "create_benefits_plan",
     "Create a benefits plan (HR Dir/Finance approval)."),
    ("update_benefits_plan.py",     "UpdateBenefitsPlan",      "update_benefits_plan",
     "Update fields on a benefits plan (with approvals)."),
    ("enroll_benefit.py",           "EnrollBenefit",           "enroll_benefit",
     "Enroll an employee into a benefits plan."),
    ("terminate_benefit.py",        "TerminateBenefit",        "terminate_benefit",
     "Deactivate an employee benefits enrollment."),
    ("record_approval.py",          "RecordApproval",          "record_approval",
     "Insert a generic approval record."),
    ("approve_item.py",             "ApproveItem",             "approve_item",
     "Approve an approval item by id."),
    ("reject_item.py",              "RejectItem",              "reject_item",
     "Reject an approval item by id."),
    ("create_training_program.py",  "CreateTrainingProgram",   "create_training_program",
     "Create a training program (mandatory flag)."),
    ("enroll_training.py",          "EnrollTraining",          "enroll_training",
     "Enroll employee in a training program."),
    ("complete_training_prog.py",   "CompleteTrainingProg",    "complete_training_prog",
     "Mark completion for a training enrollment."),
    ("start_performance_review.py", "StartPerformanceReview",  "start_performance_review",
     "Start a performance review record."),
    ("submit_approve_review.py",    "SubmitApproveReview",     "submit_approve_review",
     "Submit or approve a review (HR Manager approval)."),
]

INTERFACES = {
    1: IF1,
    2: IF2,
    3: IF3,
    4: IF4,
    5: IF5,
}

# ---------- COMMON TOOL TEMPLATE (validation-first & audit logging) ----------

TOOL_FILE_TEMPLATE = """\
import json
from typing import Any, Dict, Optional
from tau_bench.envs.tool import Tool

# Utility: deterministic string id generator (max existing key + 1)
def _next_id(table: Dict[str, Any]) -> str:
    if not table:
        return "1"
    return str(max(int(k) for k in table.keys()) + 1)

def _halt(msg: str) -> str:
    return json.dumps({{"error": f"Halt: {{msg}}"}})

def _write_audit(data: Dict[str, Any], user_id: str, table: str, action: str, record_id: str,
                 field: Optional[str]=None, old_value: Optional[str]=None, new_value: Optional[str]=None):
    logs = data.get("audit_logs", {{}})
    audit_id = _next_id(logs)
    logs[audit_id] = {{
        "audit_id": audit_id,
        "user_id": user_id,
        "table_name": table,
        "action": action,
        "record_id": record_id,
        "field": field,
        "old_value": old_value,
        "new_value": new_value,
        "timestamp": "2025-10-01T00:00:00Z"
    }}
    data["audit_logs"] = logs

class {class_name}(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # NOTE: Keep implementations concise in the scaffold; you can refine logic later.
        # Basic validation & example mutation per SOP expectations.

        # Example: look up user if 'acting_user_id' provided; else passthrough
        acting_user_id = kwargs.get("acting_user_id", "")
        users = data.get("users", {{}})

        if acting_user_id and acting_user_id not in users:
            return _halt("Invalid acting user")

        # ---- PLACEHOLDER / SAMPLE LOGIC (EDIT PER TOOL) ----
        # Create a small echo of inputs so you can test wiring
        result = {{"tool": "{tool_name}", "ok": True, "received": kwargs}}
        # Always write an audit row to match SOP "every change must log".
        _write_audit(data, acting_user_id or "system", "meta", "read", "{tool_name}")

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {{
            "type": "function",
            "function": {{
                "name": "{tool_name}",
                "description": "{description}",
                "parameters": {{
                    "type": "object",
                    "properties": {{
                        "acting_user_id": {{
                            "type": "string",
                            "description": "User performing the action (for authorization & audit)"
                        }},
                        "payload": {{
                            "type": "object",
                            "description": "Tool-specific payload (fields vary by tool)"
                        }}
                    }},
                    "required": []
                }}
            }}
        }}
"""

INIT_TEMPLATE = """\
# __init__.py for interface {idx}
from typing import List, Type
from tau_bench.envs.tool import Tool

{imports}

ALL_TOOLS_INTERFACE_{idx}: List[Type[Tool]] = [
{class_list}
]
"""

TOOLS_INIT_TOP = """\
# tools/__init__.py — export all interface tool lists
try:
    from tau_bench.envs.payroll_management.tools.interface_1 import ALL_TOOLS_INTERFACE_1
    from tau_bench.envs.payroll_management.tools.interface_2 import ALL_TOOLS_INTERFACE_2
    from tau_bench.envs.payroll_management.tools.interface_3 import ALL_TOOLS_INTERFACE_3
    from tau_bench.envs.payroll_management.tools.interface_4 import ALL_TOOLS_INTERFACE_4
    from tau_bench.envs.payroll_management.tools.interface_5 import ALL_TOOLS_INTERFACE_5
except ModuleNotFoundError:
    from .interface_1 import ALL_TOOLS_INTERFACE_1
    from .interface_2 import ALL_TOOLS_INTERFACE_2
    from .interface_3 import ALL_TOOLS_INTERFACE_3
    from .interface_4 import ALL_TOOLS_INTERFACE_4
    from .interface_5 import ALL_TOOLS_INTERFACE_5
"""

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def write(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    # Create interface folders and files
    for idx, spec in INTERFACES.items():
        iface_dir = os.path.join(ROOT, f"interface_{idx}")
        ensure_dir(iface_dir)

        # Generate each tool file
        class_names = []
        import_lines = []
        for filename, class_name, tool_name, description in spec:
            class_names.append(class_name)
            import_lines.append(f"from .{filename.replace('.py','')} import {class_name}")
            code = TOOL_FILE_TEMPLATE.format(
                class_name=class_name,
                tool_name=tool_name,
                description=description.replace('"', '\\"')
            )
            write(os.path.join(iface_dir, filename), code)

        # __init__.py per interface
        class_list = ",\n".join([f"    {cn}" for cn in class_names])
        init_code = INIT_TEMPLATE.format(
            idx=idx,
            imports="\n".join(import_lines),
            class_list=class_list
        )
        write(os.path.join(iface_dir, "__init__.py"), init_code)

    # Top-level tools/__init__.py (exports ALL_TOOLS_INTERFACE_1..5)
    write(os.path.join(ROOT, "__init__.py"), TOOLS_INIT_TOP)

if __name__ == "__main__":
    main()

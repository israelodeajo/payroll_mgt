# Copyright Sierra
# payroll_management domain data loader

import json
import os
from typing import Dict, Any

# List of all JSON files that make up the HR Payroll / Payment domain
DATA_FILES = [
    "users.json",
    "employees.json",
    "timesheets.json",
    "payroll_runs.json",
    "payroll_line_items.json",
    "deductions.json",
    "employee_deductions.json",
    "payroll_corrections.json",
    "benefits_plans.json",
    "employee_benefits.json",
    "expense_reimbursements.json",
    "leave_requests.json",
    "approvals.json",
    "audit_logs.json",
    "vendors.json",
    "vendor_payments.json",
]

def load_data(base_dir: str = None) -> Dict[str, Any]:
    """
    Load all seeded JSON data for the payroll_management domain.

    Args:
        base_dir: optional override path. Defaults to this package directory.

    Returns:
        Dict mapping table_name (without .json) -> dict-of-records
    """
    if base_dir is None:
        base_dir = os.path.dirname(__file__)

    data = {}
    for filename in DATA_FILES:
        path = os.path.join(base_dir, filename)
        table_name = filename.replace(".json", "")
        with open(path, "r", encoding="utf-8") as f:
            data[table_name] = json.load(f)
    return data

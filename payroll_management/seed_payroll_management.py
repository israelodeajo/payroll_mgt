#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Seeding script for payroll_management domain.
- Generates JSON files for all tables with valid FKs and consistent timestamps.
- All IDs are incremental strings starting from "1".
- Each table has the same number of rows (N), configurable below.
- Deterministic via fixed random seed.

Run:
  pip install Faker
  python3 seed_payroll_management.py

Output:
  ./data/*.json (dict-of-objects where key == primary id string)
"""

import json
import os
import random
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP

from faker import Faker

# ---------------------- CONFIG ----------------------

N = 25  # rows per table (same across all tables)
OUT_DIR = os.path.join(os.path.dirname(__file__), "data")
RANDOM_SEED = 424242
BASE_TS = datetime(2025, 9, 1, 10, 0, 0)  # base timestamp
FIXED_PROCESSED_TS = datetime(2025, 9, 15, 12, 0, 0)  # used for processed/paid fields

# Enums (must match schema exactly)
USER_ROLES = [
    "employee", "manager", "payroll_administrator", "finance_officer",
    "hr_director", "it_administrator", "compliance_officer"
]
USER_STATUS = ["active", "inactive", "suspended"]
PAY_FREQ = ["weekly", "biweekly", "semimonthly", "monthly"]
TIMESHEET_STATUS = ["submitted", "approved", "rejected"]
PAYROLL_RUN_STATUS = ["draft", "approved", "paid", "failed"]
BENEFIT_PLAN_TYPE = ["health", "dental", "vision", "retirement", "commuter", "life"]
LIFECYCLE_STATUS = ["active", "inactive", "pending"]
DEDUCTION_TYPE = ["tax", "social_security", "benefit", "garnishment", "custom"]
CALC_METHOD = ["percent", "fixed"]
REIMBURSEMENT_STATUS = ["submitted", "approved", "rejected", "paid"]
LEAVE_TYPE = ["annual", "sick", "fmla", "personal", "bereavement", "jury_duty"]
APPROVAL_STATUS = ["approved", "rejected", "pending"]
AUDIT_ACTION = ["create", "read", "update", "delete", "approve", "reject", "login", "logout", "export"]
VENDOR_STATUS = ["active", "inactive", "blocked"]
PAYMENT_STATUS = ["submitted", "approved", "rejected", "paid", "failed"]

# ---------------------- SETUP ----------------------

random.seed(RANDOM_SEED)
fake = Faker()
Faker.seed(RANDOM_SEED)

os.makedirs(OUT_DIR, exist_ok=True)

def to_money(x):
    return float(Decimal(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

def id_str(i: int) -> str:
    return str(i)

def ts_offset(hours: int = 0, days: int = 0) -> str:
    return (BASE_TS + timedelta(days=days, hours=hours)).isoformat()

def ensure_updated_after(created: str, min_delta_hours: int = 0) -> str:
    c = datetime.fromisoformat(created)
    u = c + timedelta(hours=max(1, min_delta_hours))
    return u.isoformat()

def pick(seq):
    return random.choice(seq)

def cycle_pick(seq, idx):
    return seq[idx % len(seq)]

# ---------------------- TABLE CONTAINERS ----------------------

users = {}
employees = {}
timesheets = {}
payroll_runs = {}
payroll_line_items = {}
deductions = {}
employee_deductions = {}
payroll_corrections = {}
benefits_plans = {}
employee_benefits = {}
expense_reimbursements = {}
leave_requests = {}
approvals = {}
audit_logs = {}
vendors = {}
vendor_payments = {}

# ---------------------- USERS ----------------------
# Ensure enough of each elevated role exists for valid approvals
role_distribution = (
    ["employee"] * max(8, N // 2) +
    ["manager"] * max(4, N // 6) +
    ["payroll_administrator"] * max(3, N // 10) +
    ["finance_officer"] * max(3, N // 10) +
    ["hr_director"] * max(2, N // 12) +
    ["it_administrator"] * max(2, N // 12) +
    ["compliance_officer"] * max(2, N // 12)
)
# Truncate/expand to exactly N
while len(role_distribution) < N:
    role_distribution.append("employee")
role_distribution = role_distribution[:N]
random.shuffle(role_distribution)

for i in range(1, N + 1):
    uid = id_str(i)
    role = role_distribution[i - 1]
    email = fake.unique.email()
    created_at = ts_offset(hours=i)
    updated_at = ensure_updated_after(created_at, min_delta_hours=1)
    users[uid] = {
        "user_id": uid,
        "email": email,
        "full_name": fake.name(),
        "role": role,
        "status": "active",
        "created_at": created_at,
        "updated_at": updated_at,
    }

# Helper pools by role
managers_pool = [u for u in users.values() if u["role"] == "manager"]
finance_pool = [u for u in users.values() if u["role"] == "finance_officer"]
hr_directors_pool = [u for u in users.values() if u["role"] == "hr_director"]
payroll_admin_pool = [u for u in users.values() if u["role"] == "payroll_administrator"]

# ---------------------- EMPLOYEES ----------------------
# Tie first N employees to first N users (regardless of their roles)
for i in range(1, N + 1):
    eid = id_str(i)
    user_id = id_str(i)
    manager_user_id = random.choice(managers_pool)["user_id"] if managers_pool else None
    created_at = ts_offset(days=i // 2)
    updated_at = ensure_updated_after(created_at, 3)
    employees[eid] = {
        "employee_id": eid,
        "user_id": user_id,
        "manager_user_id": manager_user_id,
        "department": random.choice(["Engineering", "HR", "Finance", "Operations", "Sales", "Support"]),
        "hire_date": (datetime(2024, 1, 1) + timedelta(days=i * 3)).date().isoformat(),
        "employment_status": random.choice(["active", "on_leave", "terminated"]) if i % 11 == 0 else "active",
        "salary_base": to_money(random.randint(60000, 140000)),
        "pay_frequency": pick(PAY_FREQ),
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- TIMESHEETS ----------------------
# 1 timesheet per employee (≤3 rule satisfied)
for i in range(1, N + 1):
    tid = id_str(i)
    emp_id = id_str(((i - 1) % N) + 1)
    work_date = (datetime(2025, 8, 1) + timedelta(days=i)).date().isoformat()
    clock_in = ts_offset(days=30 + i, hours=9)
    clock_out = ts_offset(days=30 + i, hours=17)
    total_hours = 8.0
    approver_user_id = random.choice(payroll_admin_pool)["user_id"] if payroll_admin_pool else None
    created_at = ts_offset(days=30 + i, hours=18)
    updated_at = ensure_updated_after(created_at, 1)
    timesheets[tid] = {
        "timesheet_id": tid,
        "employee_id": emp_id,
        "work_date": work_date,
        "clock_in": clock_in,
        "clock_out": clock_out,
        "total_hours": total_hours,
        "status": cycle_pick(TIMESHEET_STATUS, i),
        "approver_user_id": approver_user_id,
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- PAYROLL RUNS ----------------------
for i in range(1, N + 1):
    rid = id_str(i)
    period_start = (datetime(2025, 8, 1) + timedelta(days=(i - 1) * 14)).date()
    period_end = period_start + timedelta(days=13)
    initiated_by = random.choice(payroll_admin_pool)["user_id"] if payroll_admin_pool else id_str(1)
    status = cycle_pick(PAYROLL_RUN_STATUS, i)
    approved_by = random.choice(finance_pool)["user_id"] if status in ("approved", "paid") and finance_pool else None
    processed_at = FIXED_PROCESSED_TS.isoformat() if status in ("approved", "paid") else None
    created_at = ts_offset(days=40 + i)
    updated_at = ensure_updated_after(created_at, 2)
    payroll_runs[rid] = {
        "payroll_run_id": rid,
        "period_start": period_start.isoformat(),
        "period_end": period_end.isoformat(),
        "status": status,
        "initiated_by_user_id": initiated_by,
        "approved_by_user_id": approved_by,
        "processed_at": processed_at,
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- PAYROLL LINE ITEMS ----------------------
# 1 line item per run; rotate employees
for i in range(1, N + 1):
    lid = id_str(i)
    run_id = id_str(i)
    emp_id = id_str(((i - 1) % N) + 1)
    gross = to_money(random.randint(1500, 6000))
    deductions_total = to_money(gross * random.uniform(0.1, 0.3))
    net = to_money(gross - deductions_total)
    created_at = ts_offset(days=41 + i)
    updated_at = ensure_updated_after(created_at, 1)
    payroll_line_items[lid] = {
        "line_item_id": lid,
        "payroll_run_id": run_id,
        "employee_id": emp_id,
        "gross_pay": gross,
        "total_deductions": deductions_total,
        "net_pay": net,
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- DEDUCTIONS ----------------------
for i in range(1, N + 1):
    did = id_str(i)
    dtype = cycle_pick(DEDUCTION_TYPE, i)
    method = cycle_pick(CALC_METHOD, i + 7)
    rate = 10.0 + (i % 5) if method == "percent" else 25.0 + (i % 20)
    created_at = ts_offset(days=10 + i)
    updated_at = ensure_updated_after(created_at, 1)
    deductions[did] = {
        "deduction_id": did,
        "name": f"{dtype.upper()}_{did}",
        "deduction_type": dtype,
        "method": method,
        "rate": float(rate),
        "active": True if i % 9 != 0 else False,
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- EMPLOYEE DEDUCTIONS ----------------------
# 1 mapping per row; pair employee i with deduction i
for i in range(1, N + 1):
    edid = id_str(i)
    emp_id = id_str(i)
    did = id_str(i)
    method = deductions[did]["method"]
    rate = deductions[did]["rate"]
    start_date = (datetime(2025, 1, 1) + timedelta(days=i * 5)).date().isoformat()
    end_date = None if i % 8 else (datetime(2026, 1, 1) + timedelta(days=i)).date().isoformat()
    created_at = ts_offset(days=15 + i)
    updated_at = ensure_updated_after(created_at, 1)
    employee_deductions[edid] = {
        "employee_deduction_id": edid,
        "employee_id": emp_id,
        "deduction_id": did,
        "method": method,
        "rate": float(rate),
        "start_date": start_date,
        "end_date": end_date,
        "active": True if not end_date else False,
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- PAYROLL CORRECTIONS ----------------------
for i in range(1, N + 1):
    cid = id_str(i)
    run_id = id_str(i)
    emp_id = id_str(((i - 1) % N) + 1)
    field_changed = random.choice(["gross_pay", "total_deductions", "net_pay"])
    old_value = str(round(random.uniform(1000, 6000), 2))
    new_value = str(round(float(old_value) * random.uniform(0.95, 1.05), 2))
    approved_by = random.choice(finance_pool)["user_id"] if finance_pool else None
    created_at = ts_offset(days=45 + i)
    updated_at = ensure_updated_after(created_at, 2)
    payroll_corrections[cid] = {
        "correction_id": cid,
        "payroll_run_id": run_id,
        "employee_id": emp_id,
        "reason": f"Adjustment for {field_changed}",
        "field_changed": field_changed,
        "old_value": old_value,
        "new_value": new_value,
        "approved_by_user_id": approved_by,
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- BENEFITS PLANS ----------------------
for i in range(1, N + 1):
    pid = id_str(i)
    ptype = cycle_pick(BENEFIT_PLAN_TYPE, i)
    start_date = datetime(2025, 1, 1).date().isoformat()
    end_date = None if i % 7 else datetime(2026, 12, 31).date().isoformat()
    created_at = ts_offset(days=5 + i)
    updated_at = ensure_updated_after(created_at, 1)
    benefits_plans[pid] = {
        "plan_id": pid,
        "name": f"{ptype.capitalize()} Plan {pid}",
        "plan_type": ptype,
        "status": "active" if not end_date else "inactive",
        "start_date": start_date,
        "end_date": end_date,
        "employer_contribution_pct": float(round(random.uniform(2.0, 6.0), 3)),
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- EMPLOYEE BENEFITS ----------------------
for i in range(1, N + 1):
    ebid = id_str(i)
    emp_id = id_str(i)
    plan_id = id_str(((i - 1) % N) + 1)
    status = cycle_pick(LIFECYCLE_STATUS, i)
    contribution_pct = float(round(random.uniform(0.0, 10.0), 3))
    contribution_amount = to_money(contribution_pct / 100.0 * employees[emp_id]["salary_base"] / 12.0)
    created_at = ts_offset(days=20 + i)
    updated_at = ensure_updated_after(created_at, 1)
    employee_benefits[ebid] = {
        "employee_benefit_id": ebid,
        "employee_id": emp_id,
        "plan_id": plan_id,
        "status": status,
        "contribution_pct": contribution_pct,
        "contribution_amount": float(contribution_amount),
        "beneficiary": fake.name() if random.random() < 0.6 else "",
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- EXPENSE REIMBURSEMENTS ----------------------
for i in range(1, N + 1):
    rid = id_str(i)
    emp_id = id_str(((i - 1) % N) + 1)
    amount = to_money(random.uniform(20, 500))
    status = cycle_pick(REIMBURSEMENT_STATUS, i)
    approved_by = random.choice(finance_pool)["user_id"] if status in ("approved", "paid") and finance_pool else None
    payment_date = (datetime(2025, 9, 20) + timedelta(days=i)).date().isoformat() if status == "paid" else None
    created_at = ts_offset(days=22 + i)
    updated_at = ensure_updated_after(created_at, 1)
    expense_reimbursements[rid] = {
        "reimbursement_id": rid,
        "employee_id": emp_id,
        "amount": amount,
        "description": f"Reimbursement for {fake.word()}",
        "status": status,
        "approved_by_user_id": approved_by,
        "payment_date": payment_date,
        "receipt_file_path": f"/receipts/{rid}.pdf" if random.random() < 0.8 else "",
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- LEAVE REQUESTS ----------------------
for i in range(1, N + 1):
    lrid = id_str(i)
    emp_id = id_str(((i - 1) % N) + 1)
    ltype = cycle_pick(LEAVE_TYPE, i)
    start = datetime(2025, 10, 1) + timedelta(days=i)
    end = start + timedelta(days=random.randint(1, 5))
    requested_days = (end - start).days + 1
    remaining = max(0, 15 - requested_days - (i % 5))
    status = cycle_pick(LIFECYCLE_STATUS, i + 3)
    approved_by = random.choice(managers_pool)["user_id"] if status != "pending" and managers_pool else None
    created_at = ts_offset(days=25 + i)
    updated_at = ensure_updated_after(created_at, 1)
    leave_requests[lrid] = {
        "leave_request_id": lrid,
        "employee_id": emp_id,
        "leave_type": ltype,
        "start_date": start.date().isoformat(),
        "end_date": end.date().isoformat(),
        "requested_days": requested_days,
        "status": status,
        "remaining_balance": remaining,
        "approved_by_user_id": approved_by,
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- APPROVALS ----------------------
# Mix approvals for payroll_run, reimbursement, benefits_plan
ACTIONS = ["payroll_run", "reimbursement", "benefits_plan"]
for i in range(1, N + 1):
    aid = id_str(i)
    action = cycle_pick(ACTIONS, i)
    requester = id_str(((i - 1) % N) + 1)  # some user
    # pick approver by action
    if action == "payroll_run":
        approver_pool = finance_pool or payroll_admin_pool or [users[id_str(1)]]
    elif action == "reimbursement":
        approver_pool = finance_pool or [users[id_str(1)]]
    else:
        approver_pool = hr_directors_pool or finance_pool or [users[id_str(1)]]
    approver = random.choice(approver_pool)["user_id"]
    status = cycle_pick(APPROVAL_STATUS, i)
    created_at = ts_offset(days=27 + i)
    updated_at = ensure_updated_after(created_at, 1)
    approvals[aid] = {
        "approval_id": aid,
        "action": action,
        "requested_by_user_id": requester,
        "approver_user_id": approver,
        "status": status,
        "notes": f"{action} approval {status}",
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- VENDORS ----------------------
for i in range(1, N + 1):
    vid = id_str(i)
    created_at = ts_offset(days=8 + i)
    updated_at = ensure_updated_after(created_at, 1)
    vendors[vid] = {
        "vendor_id": vid,
        "name": f"{fake.company()}",
        "tin": f"{random.randint(10_000_000, 99_999_999)}",
        "bank_account": f"ACCT-{random.randint(10000000, 99999999)}",
        "status": cycle_pick(VENDOR_STATUS, i),
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- VENDOR PAYMENTS ----------------------
for i in range(1, N + 1):
    vpid = id_str(i)
    vendor_id = id_str(i)
    status = cycle_pick(PAYMENT_STATUS, i)
    approved_by = random.choice(finance_pool)["user_id"] if status in ("approved", "paid") and finance_pool else None
    paid_at = FIXED_PROCESSED_TS.date().isoformat() if status == "paid" else None
    amount = to_money(random.uniform(200, 20000))
    created_at = ts_offset(days=12 + i)
    updated_at = ensure_updated_after(created_at, 1)
    vendor_payments[vpid] = {
        "vendor_payment_id": vpid,
        "vendor_id": vendor_id,
        "invoice_no": f"INV-{2025}{i:03d}",
        "amount": amount,
        "status": status,
        "approved_by_user_id": approved_by,
        "paid_at": paid_at,
        "created_at": created_at,
        "updated_at": updated_at,
    }

# ---------------------- AUDIT LOGS ----------------------
for i in range(1, N + 1):
    aid = id_str(i)
    user_id = id_str(((i - 1) % N) + 1)
    table_name = random.choice([
        "payroll_runs", "payroll_line_items", "employee_deductions",
        "expense_reimbursements", "leave_requests", "vendor_payments",
        "benefits_plans", "employee_benefits", "timesheets"
    ])
    action = cycle_pick(AUDIT_ACTION, i)
    record_id = id_str(((i - 1) % N) + 1)
    created_at = ts_offset(days=50 + i)
    audit_logs[aid] = {
        "audit_id": aid,
        "user_id": user_id,
        "table_name": table_name,
        "action": action,
        "record_id": record_id,
        "field": None if action in ("create", "delete") else "status",
        "old_value": None if action in ("create", "delete") else "pending",
        "new_value": None if action in ("create", "delete") else cycle_pick(["approved", "paid", "draft"], i),
        "timestamp": created_at,
    }

# ---------------------- WRITE JSON FILES ----------------------

tables = {
    "users.json": users,
    "employees.json": employees,
    "timesheets.json": timesheets,
    "payroll_runs.json": payroll_runs,
    "payroll_line_items.json": payroll_line_items,
    "deductions.json": deductions,
    "employee_deductions.json": employee_deductions,
    "payroll_corrections.json": payroll_corrections,
    "benefits_plans.json": benefits_plans,
    "employee_benefits.json": employee_benefits,
    "expense_reimbursements.json": expense_reimbursements,
    "leave_requests.json": leave_requests,
    "approvals.json": approvals,
    "audit_logs.json": audit_logs,
    "vendors.json": vendors,
    "vendor_payments.json": vendor_payments,
}

for filename, payload in tables.items():
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

print(f"✅ Seeded {len(tables)} tables to: {OUT_DIR}")

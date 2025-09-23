---

# Payroll Management Domain (Tau-Bench)

This domain implements a **realistic HR & Payroll Management environment** for Amazon’s Tau-Bench framework.
It combines **policies, SOPs, database schemas, seeded JSON data, and tool interfaces** to simulate verifiable agentic tasks around HR, payroll, and compliance.

---

## 📂 Directory Structure

```
envs/payroll_management/
│── __init__.py                # Environment loader (get_env)
│── env.py                     # MockPayrollManagementDomainEnv
│── rules.py                   # Business rules derived from HR/Payroll SOP
│── hrpolicy.md                # Policy & SOP reference document
│── wiki.md / wiki.py          # Domain description + accessor
│── data/                      # Seeded JSON DBs (faker generated)
│   ├── users.json
│   ├── employees.json
│   ├── timesheets.json
│   ├── payroll_runs.json
│   ├── payroll_line_items.json
│   ├── deductions.json
│   ├── employee_deductions.json
│   ├── payroll_corrections.json
│   ├── benefits_plans.json
│   ├── employee_benefits.json
│   ├── expense_reimbursements.json
│   ├── leave_requests.json
│   ├── approvals.json
│   ├── audit_logs.json
│   ├── vendors.json
│   └── vendor_payments.json
│── tools/                     # Tool interfaces (1–5)
│   ├── __init__.py            # Exports ALL_TOOLS_INTERFACE_1..5
│   ├── scaffold_tools.py      # Script to scaffold tool files
│   ├── interface_1/           # Provisioning & Departments
│   ├── interface_2/           # Recruiting & Interviews
│   ├── interface_3/           # Employees & Documents
│   ├── interface_4/           # Timesheets & Payroll
│   └── interface_5/           # Benefits, Approvals, Training
```

---

## 📑 Policy & SOP Coverage

All functionality derives from the **HR & Payroll Management Policy (`hrpolicy.md`)**:

* **Payroll**
  Salaries, deductions, corrections, approvals, settlements.
* **Payments**
  Vendor onboarding, invoices, dispute handling, tax compliance.
* **Benefits**
  Health, retirement, commuter plans with employee contributions.
* **Timesheets & Leave**
  Submission, approval, accrual balances, compliance.
* **Audits**
  Every action writes an entry to `audit_logs` (required by SOP).
* **Approvals**
  Manager/HR/Finance authorization checks enforced in tools.

---

## 🗄 Database Schema

The DBML schema was authored in [dbdiagram.io](https://dbdiagram.io) and exported to JSON seed data via **Faker**.
Key design choices:

* **String IDs** (`"1"`, `"2"`, …) for consistency.
* **One-to-many caps**: ≤ 3 child rows per parent (realistic).
* **Foreign keys enforced**: No orphans allowed.
* **Timestamps**: `created_at ≤ updated_at`; audit logs timestamped `2025-10-01T00:00:00Z`.
* **Enums**: Constrained to valid SOP values (e.g., `payroll_run_status = "approved"`).

---

## 🔧 Tools & Interfaces

Each interface provides **12 tools** with **overlapping functionality** but different names, enabling models to generalize across varied tool specs:

* **Interface 1** – User provisioning, departments, RBAC, audit, approvals.
* **Interface 2** – Job positions, candidates, applications, interviews, compliance.
* **Interface 3** – Employee lifecycle (onboard/offboard), profiles, docs, training, reviews.
* **Interface 4** – Timesheets, payroll runs, corrections, reimbursements, leave.
* **Interface 5** – Benefits, approvals, training, performance reviews.

### Common Features

* Imports: `json`, `typing`, `from tau_bench.envs.tool import Tool`.
* Each tool has:

  * `invoke(data, **kwargs) -> str` returning a JSON string.
  * `get_info()` describing the tool in OpenAPI-like format.
* **Audit Logging**: Every action creates an entry in `audit_logs`.
* **Validation-first**: Tools check user roles, existing records, enums before mutating data.

---

## 🚀 How to Run

1. **Install dependencies**

   ```bash
   pip install faker
   ```

2. **Generate/refresh tool files**

   ```bash
   cd envs/payroll_management/tools
   python3 scaffold_tools.py
   ```

3. **Load data in test mode**

   ```python
   from envs.payroll_management.data import load_data
   db = load_data()
   print(db["users"].keys())
   ```

4. **Use in Tau-Bench**
   Import via `MockPayrollManagementDomainEnv` in `env.py`, which bundles:

   * Seed data
   * Business rules (`rules.py`)
   * Tool interfaces (1–5)
   * Wiki + HR policy

---


## 🔒 Compliance & Ethics

* Payroll, vendor, and employee data must remain confidential.
* Tools enforce **authorization discipline** (only managers/finance/HR can approve).
* All workflows log to `audit_logs` for traceability.
* SOPs align with **U.S. labor, tax, and payment compliance**.

---

📖 This domain provides a **full-stack HR & Payroll sandbox** for agentic task benchmarking — combining **realistic enterprise workflows** with **policy-driven constraints**.

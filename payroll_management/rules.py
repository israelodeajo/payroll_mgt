# Business rules derived from HR Payroll Policy

RULES = {
    "payroll_processing": [
        "All payroll runs must be validated before execution.",
        "Finance Officer approval required before payroll disbursement.",
        "No payroll record can be modified without audit logging.",
    ],
    "reimbursements": [
        "Reimbursements must be linked to a valid employee ID.",
        "Only Finance Officers may approve reimbursements.",
        "Status changes must follow the sequence: submitted → approved → paid.",
    ],
    "leave_requests": [
        "Leave requests must not exceed available balance.",
        "All leave requests require manager approval before HR processing.",
    ],
    "data_security": [
        "Payroll data must be stored securely with restricted access.",
        "Audit logs cannot be altered or deleted.",
    ],
}

# __init__.py for interface 4
from typing import List, Type
from tau_bench.envs.tool import Tool

from .submit_timesheet import SubmitTimesheet
from .approve_timesheet import ApproveTimesheet
from .start_payroll_run import StartPayrollRun
from .approve_payroll_run import ApprovePayrollRun
from .pay_payroll_run import PayPayrollRun
from .correct_payroll import CorrectPayroll
from .request_leave import RequestLeave
from .process_reimbursement import ProcessReimbursement
from .update_reimbursement import UpdateReimbursement
from .list_timesheets import ListTimesheets
from .compute_leave_balance import ComputeLeaveBalance
from .gen_payroll_line_items import GenPayrollLineItems

ALL_TOOLS_INTERFACE_4: List[Type[Tool]] = [
    SubmitTimesheet,
    ApproveTimesheet,
    StartPayrollRun,
    ApprovePayrollRun,
    PayPayrollRun,
    CorrectPayroll,
    RequestLeave,
    ProcessReimbursement,
    UpdateReimbursement,
    ListTimesheets,
    ComputeLeaveBalance,
    GenPayrollLineItems
]

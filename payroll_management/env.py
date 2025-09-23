# Copyright Sierra

from typing import Optional, Union
from tau_bench.envs.base import Env
from tau_bench.envs.user import UserStrategy

from tau_bench.envs.payroll_management.data import load_data
from tau_bench.envs.payroll_management.rules import RULES
from tau_bench.envs.payroll_management.tools import (
    ALL_TOOLS_INTERFACE_1,
    ALL_TOOLS_INTERFACE_2,
    ALL_TOOLS_INTERFACE_3,
    ALL_TOOLS_INTERFACE_4,
    ALL_TOOLS_INTERFACE_5,
)
from tau_bench.envs.payroll_management.hrpolicy import HR_POLICY


class MockPayrollManagementDomainEnv(Env):
    """
    Mock Payroll Management Environment

    Provides APIs for managing payroll, deductions, reimbursements, 
    vendor payments, and benefits, while enforcing compliance and approval workflows.
    """

    def __init__(
        self,
        user_strategy: Union[str, UserStrategy],
        user_model: str,
        task_split: str,
        user_provider: Optional[str] = None,
        task_index: Optional[int] = None,
    ):
        super().__init__(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
        self.data = load_data()
        self.rules = RULES
        self.policy = HR_POLICY
        self.tools = {
            "interface_1": ALL_TOOLS_INTERFACE_1,
            "interface_2": ALL_TOOLS_INTERFACE_2,
            "interface_3": ALL_TOOLS_INTERFACE_3,
            "interface_4": ALL_TOOLS_INTERFACE_4,
            "interface_5": ALL_TOOLS_INTERFACE_5,
        }

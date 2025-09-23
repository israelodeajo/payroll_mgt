# __init__.py for interface 1
from typing import List, Type
from tau_bench.envs.tool import Tool

from .register_account import RegisterAccount
from .create_unit import CreateUnit
from .revise_unit import ReviseUnit
from .record_audit import RecordAudit
from .add_rbac_role import AddRbacRole
from .suspend_user import SuspendUser
from .activate_user import ActivateUser
from .request_admin_approval import RequestAdminApproval
from .approve_request import ApproveRequest
from .reject_request import RejectRequest
from .list_units import ListUnits
from .lookup_user import LookupUser

ALL_TOOLS_INTERFACE_1: List[Type[Tool]] = [
    RegisterAccount,
    CreateUnit,
    ReviseUnit,
    RecordAudit,
    AddRbacRole,
    SuspendUser,
    ActivateUser,
    RequestAdminApproval,
    ApproveRequest,
    RejectRequest,
    ListUnits,
    LookupUser
]

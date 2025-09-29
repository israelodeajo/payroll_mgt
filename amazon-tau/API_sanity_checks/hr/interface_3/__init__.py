# __init__.py for interface 3
from typing import List, Type
from tau_bench.envs.tool import Tool

from .onboard_employee import OnboardEmployee
from .update_employee_profile import UpdateEmployeeProfile
from .offboard_employee import OffboardEmployee
from .upload_document import UploadDocument
from .set_manager import SetManager
from .deactivate_user_account import DeactivateUserAccount
from .verify_compliance_docs import VerifyComplianceDocs
from .assign_training import AssignTraining
from .complete_training import CompleteTraining
from .start_review_cycle import StartReviewCycle
from .submit_review import SubmitReview
from .list_employee_docs import ListEmployeeDocs

ALL_TOOLS_INTERFACE_3: List[Type[Tool]] = [
    OnboardEmployee,
    UpdateEmployeeProfile,
    OffboardEmployee,
    UploadDocument,
    SetManager,
    DeactivateUserAccount,
    VerifyComplianceDocs,
    AssignTraining,
    CompleteTraining,
    StartReviewCycle,
    SubmitReview,
    ListEmployeeDocs
]

# __init__.py for interface 5
from typing import List, Type
from tau_bench.envs.tool import Tool

from .create_benefits_plan import CreateBenefitsPlan
from .update_benefits_plan import UpdateBenefitsPlan
from .enroll_benefit import EnrollBenefit
from .terminate_benefit import TerminateBenefit
from .record_approval import RecordApproval
from .approve_item import ApproveItem
from .reject_item import RejectItem
from .create_training_program import CreateTrainingProgram
from .enroll_training import EnrollTraining
from .complete_training_prog import CompleteTrainingProg
from .start_performance_review import StartPerformanceReview
from .submit_approve_review import SubmitApproveReview

ALL_TOOLS_INTERFACE_5: List[Type[Tool]] = [
    CreateBenefitsPlan,
    UpdateBenefitsPlan,
    EnrollBenefit,
    TerminateBenefit,
    RecordApproval,
    ApproveItem,
    RejectItem,
    CreateTrainingProgram,
    EnrollTraining,
    CompleteTrainingProg,
    StartPerformanceReview,
    SubmitApproveReview
]

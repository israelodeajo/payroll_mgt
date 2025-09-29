# __init__.py for interface 2
from typing import List, Type
from tau_bench.envs.tool import Tool

from .create_position import CreatePosition
from .publish_opening import PublishOpening
from .close_opening import CloseOpening
from .add_candidate import AddCandidate
from .file_application import FileApplication
from .advance_stage import AdvanceStage
from .book_interview import BookInterview
from .finalize_interview import FinalizeInterview
from .withdraw_application import WithdrawApplication
from .link_application_doc import LinkApplicationDoc
from .list_open_positions import ListOpenPositions
from .flag_compliance_case import FlagComplianceCase

ALL_TOOLS_INTERFACE_2: List[Type[Tool]] = [
    CreatePosition,
    PublishOpening,
    CloseOpening,
    AddCandidate,
    FileApplication,
    AdvanceStage,
    BookInterview,
    FinalizeInterview,
    WithdrawApplication,
    LinkApplicationDoc,
    ListOpenPositions,
    FlagComplianceCase
]

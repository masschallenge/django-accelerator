import swapper

from accelerator.models.judge_panel_assignment_manager import (
    JudgePanelAssignmentManager,
)
from accelerator_abstract.models.base_judge_panel_assignment import (
    BaseJudgePanelAssignment
)


class JudgePanelAssignment(BaseJudgePanelAssignment):
    class Meta(BaseJudgePanelAssignment.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgePanelAssignment.Meta.app_label, "JudgePanelAssignment")

    objects = JudgePanelAssignmentManager()

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_judge_panel_assignment import (
    BaseJudgePanelAssignment
)


class JudgePanelAssignment(BaseJudgePanelAssignment):
    class Meta(BaseJudgePanelAssignment.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgePanelAssignment.Meta.app_label, "JudgePanelAssignment")

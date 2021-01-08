# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_judge_panel_assignment import (
    BaseJudgePanelAssignment
)


class JudgePanelAssignment(BaseJudgePanelAssignment):
    class Meta(BaseJudgePanelAssignment.Meta):
        swappable = False

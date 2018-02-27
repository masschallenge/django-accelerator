# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_judge_feedback_component import (
    BaseJudgeFeedbackComponent
)


class JudgeFeedbackComponent(BaseJudgeFeedbackComponent):
    class Meta(BaseJudgeFeedbackComponent.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgeFeedbackComponent.Meta.app_label,
            "JudgeFeedbackComponent")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BaseJudgeApplicationFeedback


class JudgeApplicationFeedback(BaseJudgeApplicationFeedback):
    class Meta(BaseJudgeApplicationFeedback.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgeApplicationFeedback.Meta.app_label,
            "JudgeApplicationFeedback")

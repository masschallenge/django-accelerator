# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseJudgeRoundCommitment


class JudgeRoundCommitment(BaseJudgeRoundCommitment):
    class Meta(BaseJudgeRoundCommitment.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgeRoundCommitment.Meta.app_label, "JudgeRoundCommitment")

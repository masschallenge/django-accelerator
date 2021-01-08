# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseJudgeRoundCommitment


class JudgeRoundCommitment(BaseJudgeRoundCommitment):
    class Meta(BaseJudgeRoundCommitment.Meta):
        swappable = False

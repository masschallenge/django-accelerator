# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_judging_round import BaseJudgingRound


class JudgingRound(BaseJudgingRound):
    class Meta(BaseJudgingRound.Meta):
        swappable = False

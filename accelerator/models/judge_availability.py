# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseJudgeAvailability


class JudgeAvailability(BaseJudgeAvailability):
    class Meta(BaseJudgeAvailability.Meta):
        swappable = False

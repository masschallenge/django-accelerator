# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseJudgingFormElement


class JudgingFormElement(BaseJudgingFormElement):
    class Meta(BaseJudgingFormElement.Meta):
        swappable = False

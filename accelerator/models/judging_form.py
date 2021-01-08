# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseJudgingForm


class JudgingForm(BaseJudgingForm):
    class Meta(BaseJudgingForm.Meta):
        swappable = False

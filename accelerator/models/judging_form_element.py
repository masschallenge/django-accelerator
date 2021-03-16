# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseJudgingFormElement


class JudgingFormElement(BaseJudgingFormElement):
    class Meta(BaseJudgingFormElement.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgingFormElement.Meta.app_label, "JudgingFormElement")

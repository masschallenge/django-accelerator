# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BasePartnerJudgingInstructions


class PartnerJudgingInstructions(BasePartnerJudgingInstructions):
    class Meta(BasePartnerJudgingInstructions.Meta):
        swappable = swapper.swappable_setting(
            BasePartnerJudgingInstructions.Meta.app_label,
            "PartnerJudgingInstructions")

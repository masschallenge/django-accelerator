# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BasePartnerJudgeApplicationAssignment


class PartnerJudgeApplicationAssignment(BasePartnerJudgeApplicationAssignment):
    class Meta(BasePartnerJudgeApplicationAssignment.Meta):
        swappable = swapper.swappable_setting(
            BasePartnerJudgeApplicationAssignment.Meta.app_label,
            "PartnerJudgeApplicationAssignment")

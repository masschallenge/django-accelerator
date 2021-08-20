# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import swapper

from accelerator_abstract.models import BasePartnerJudgingRoundChallenge


class PartnerJudgingRoundChallenge(BasePartnerJudgingRoundChallenge):
    class Meta(BasePartnerJudgingRoundChallenge.Meta):
        swappable = swapper.swappable_setting(
            BasePartnerJudgingRoundChallenge.Meta.app_label,
            "PartnerJudgingRoundChallenge")


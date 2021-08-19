# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import swapper

from accelerator_abstract.models import BasePartnerJudgingRoundChallenge


class PartnerJudgingRoundChallenge(BasePartnerJudgingRoundChallenge):
    class Meta(BaseJudgingRoundChallenge.Meta):
        swappable = swapper.swappable_setting(
            BaseClearance.Meta.app_label, "PartnerJudgingRoundChallenge")


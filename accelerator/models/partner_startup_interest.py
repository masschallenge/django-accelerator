# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import swapper

from accelerator_abstract.models import BasePartnerStartupInterest


class PartnerStartupInterest(BasePartnerStartupInterest):
    class Meta(BasePartnerStartupInterest.Meta):
        swappable = swapper.swappable_setting(
            BasePartnerStartupInterest.Meta.app_label,
            "PartnerStartupInterest")

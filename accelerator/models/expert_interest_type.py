# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BaseExpertInterestType


class ExpertInterestType(BaseExpertInterestType):
    class Meta(BaseExpertInterestType.Meta):
        swappable = swapper.swappable_setting(
            BaseExpertInterestType.Meta.app_label, "ExpertInterestType")

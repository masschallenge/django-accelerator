# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BaseProgramPartnerType


class ProgramPartnerType(BaseProgramPartnerType):
    class Meta(BaseProgramPartnerType.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramPartnerType.Meta.app_label, "ProgramPartnerType")

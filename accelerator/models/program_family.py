# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BaseProgramFamily


class ProgramFamily(BaseProgramFamily):
    class Meta(BaseProgramFamily.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramFamily.Meta.app_label, "ProgramFamily")

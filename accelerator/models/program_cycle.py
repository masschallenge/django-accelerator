# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_program_cycle import BaseProgramCycle


class ProgramCycle(BaseProgramCycle):
    class Meta(BaseProgramCycle.Meta):
        swappable = swapper.swappable_setting(BaseProgramCycle.Meta.app_label,
                                              "ProgramCycle")

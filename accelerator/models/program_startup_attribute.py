# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_program_startup_attribute import (
    BaseProgramStartupAttribute
)


class ProgramStartupAttribute(BaseProgramStartupAttribute):
    class Meta(BaseProgramStartupAttribute.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramStartupAttribute.Meta.app_label,
            "ProgramStartupAttribute")

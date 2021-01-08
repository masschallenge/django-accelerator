# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_program_startup_status import (
    BaseProgramStartupStatus
)


class ProgramStartupStatus(BaseProgramStartupStatus):
    class Meta(BaseProgramStartupStatus.Meta):
        swappable = False

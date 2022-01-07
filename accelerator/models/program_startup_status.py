from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_program_startup_status import (
    BaseProgramStartupStatus
)


class ProgramStartupStatus(BaseProgramStartupStatus):
    class Meta(BaseProgramStartupStatus.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramStartupStatus.Meta.app_label, "ProgramStartupStatus")

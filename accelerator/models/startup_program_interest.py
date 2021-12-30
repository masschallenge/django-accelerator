from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_startup_program_interest import (
    BaseStartupProgramInterest
)


class StartupProgramInterest(BaseStartupProgramInterest):
    class Meta(BaseStartupProgramInterest.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupProgramInterest.Meta.app_label,
            "StartupProgramInterest")

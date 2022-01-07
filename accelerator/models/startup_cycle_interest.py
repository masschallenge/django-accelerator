from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_startup_cycle_interest import (
    BaseStartupCycleInterest
)


class StartupCycleInterest(BaseStartupCycleInterest):
    class Meta(BaseStartupCycleInterest.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupCycleInterest.Meta.app_label, "StartupCycleInterest")

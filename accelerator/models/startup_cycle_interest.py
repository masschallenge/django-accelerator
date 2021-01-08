# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_startup_cycle_interest import (
    BaseStartupCycleInterest
)


class StartupCycleInterest(BaseStartupCycleInterest):
    class Meta(BaseStartupCycleInterest.Meta):
        swappable = False

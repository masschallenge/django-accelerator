# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_startup_status import BaseStartupStatus


class StartupStatus(BaseStartupStatus):
    class Meta(BaseStartupStatus.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupStatus.Meta.app_label, "StartupStatus")

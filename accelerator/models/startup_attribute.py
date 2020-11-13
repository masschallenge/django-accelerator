# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_startup_attribute import (
    BaseStartupAttribute
)


class StartupAttribute(BaseStartupAttribute):
    class Meta(BaseStartupAttribute.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupAttribute.Meta.app_label, "StartupAttribute")

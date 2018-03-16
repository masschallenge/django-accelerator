# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_startup_override_grant import (
    BaseStartupOverrideGrant
)


class StartupOverrideGrant(BaseStartupOverrideGrant):
    class Meta(BaseStartupOverrideGrant.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupOverrideGrant.Meta.app_label, "StartupOverrideGrant")

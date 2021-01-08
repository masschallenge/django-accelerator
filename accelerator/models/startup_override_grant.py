# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_startup_override_grant import (
    BaseStartupOverrideGrant
)


class StartupOverrideGrant(BaseStartupOverrideGrant):
    class Meta(BaseStartupOverrideGrant.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_startup_role import BaseStartupRole


class StartupRole(BaseStartupRole):
    class Meta(BaseStartupRole.Meta):
        swappable = False

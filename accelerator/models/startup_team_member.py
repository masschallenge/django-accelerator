# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_startup_team_member import (
    BaseStartupTeamMember
)


class StartupTeamMember(BaseStartupTeamMember):
    class Meta(BaseStartupTeamMember.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupTeamMember.Meta.app_label, "StartupTeamMember")

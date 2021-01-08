# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_startup_team_member import (
    BaseStartupTeamMember
)


class StartupTeamMember(BaseStartupTeamMember):
    class Meta(BaseStartupTeamMember.Meta):
        swappable = False

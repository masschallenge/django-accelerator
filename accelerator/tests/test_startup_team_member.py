# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import StartupTeamMemberFactory


class TestStartupTeamMember(TestCase):
    def test_str(self):
        team_member = StartupTeamMemberFactory()
        assert str(team_member.startup) in str(team_member)
        assert str(team_member.user) in str(team_member)

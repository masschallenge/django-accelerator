# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import PartnerTeamMemberFactory


class TestPartnerTeamMember(TestCase):

    def test_str(self):
        partner_team_member = PartnerTeamMemberFactory()
        assert str(partner_team_member.team_member) in str(partner_team_member)
        assert partner_team_member.partner.name in str(partner_team_member)

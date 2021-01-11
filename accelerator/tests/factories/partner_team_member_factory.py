# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import SubFactory
from factory.django import DjangoModelFactory

from .entrepreneur_factory import EntrepreneurFactory
from .partner_factory import PartnerFactory

from accelerator.models import PartnerTeamMember


class PartnerTeamMemberFactory(DjangoModelFactory):
    class Meta:
        model = PartnerTeamMember

    partner = SubFactory(PartnerFactory)
    team_member = SubFactory(EntrepreneurFactory)
    partner_administrator = False

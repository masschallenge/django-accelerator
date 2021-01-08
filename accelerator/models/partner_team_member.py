# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BasePartnerTeamMember


class PartnerTeamMember(BasePartnerTeamMember):
    class Meta(BasePartnerTeamMember.Meta):
        swappable = False

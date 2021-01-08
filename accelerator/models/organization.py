# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseOrganization


class Organization(BaseOrganization):
    class Meta(BaseOrganization.Meta):
        swappable = False

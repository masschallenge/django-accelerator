# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseProgramPartnerType


class ProgramPartnerType(BaseProgramPartnerType):
    class Meta(BaseProgramPartnerType.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseLegalCheck


class LegalCheck(BaseLegalCheck):
    class Meta(BaseLegalCheck.Meta):
        swappable = False

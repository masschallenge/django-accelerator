# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseUserLegalCheck


class UserLegalCheck(BaseUserLegalCheck):
    class Meta(BaseUserLegalCheck.Meta):
        swappable = False

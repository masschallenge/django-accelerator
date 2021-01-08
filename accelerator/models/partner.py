# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BasePartner


class Partner(BasePartner):
    class Meta(BasePartner.Meta):
        swappable = False

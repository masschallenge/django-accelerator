# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BasePartner


class Partner(BasePartner):
    class Meta(BasePartner.Meta):
        swappable = swapper.swappable_setting(
            BasePartner.Meta.app_label, "Partner")

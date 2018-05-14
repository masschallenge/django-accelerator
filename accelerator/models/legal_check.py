# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseLegalCheck


class LegalCheck(BaseLegalCheck):
    class Meta(BaseLegalCheck.Meta):
        swappable = swapper.swappable_setting(
            BaseLegalCheck.Meta.app_label, 'LegalCheck')

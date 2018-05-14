# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseLegalCheckAcceptance


class LegalCheckAcceptance(BaseLegalCheckAcceptance):
    class Meta(BaseLegalCheckAcceptance.Meta):
        swappable = swapper.swappable_setting(
            BaseLegalCheckAcceptance.Meta.app_label, 'LegalCheckAcceptance')

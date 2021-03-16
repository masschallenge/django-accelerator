# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseProgramPartner


class ProgramPartner(BaseProgramPartner):
    class Meta(BaseProgramPartner.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramPartner.Meta.app_label, "ProgramPartner")

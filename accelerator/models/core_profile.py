# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_core_profile import BaseCoreProfile
from accelerator.models.judging_round import JudgingRound
from accelerator.models.user_role import UserRole

class CoreProfile(BaseCoreProfile):
    class Meta(BaseCoreProfile.Meta):
        swappable = swapper.swappable_setting(
            BaseCoreProfile.Meta.app_label, "CoreProfile")
        abstract = True

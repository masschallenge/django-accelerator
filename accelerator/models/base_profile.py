# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_base_profile import BaseBaseProfile


class BaseProfile(BaseBaseProfile):
    class Meta(BaseBaseProfile.Meta):
        swappable = swapper.swappable_setting(
            BaseBaseProfile.Meta.app_label, "BaseProfile")
        abstract = True

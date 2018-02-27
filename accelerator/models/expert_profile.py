# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseExpertProfile


class ExpertProfile(BaseExpertProfile):
    class Meta(BaseExpertProfile.Meta):
        swappable = swapper.swappable_setting(
            BaseExpertProfile.Meta.app_label, "ExpertProfile")

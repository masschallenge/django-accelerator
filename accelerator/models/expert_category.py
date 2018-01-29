# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseExpertCategory


class ExpertCategory(BaseExpertCategory):
    class Meta(BaseExpertCategory.Meta):
        swappable = swapper.swappable_setting(
            BaseExpertCategory.Meta.app_label, "ExpertCategory")

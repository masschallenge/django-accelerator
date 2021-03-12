# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import swapper

from ...accelerator_abstract.models import BaseIndustry


class Industry(BaseIndustry):
    class Meta(BaseIndustry.Meta):
        app_label = "accelerator"
        swappable = swapper.swappable_setting("accelerator", "Industry")

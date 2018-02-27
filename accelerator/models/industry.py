# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from accelerator_abstract.models import BaseIndustry


class Industry(BaseIndustry):
    class Meta(BaseIndustry.Meta):
        swappable = 'MPTT_SWAPPABLE_INDUSTRY_MODEL'

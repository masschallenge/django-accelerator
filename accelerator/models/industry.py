# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from accelerator_abstract.models import BaseIndustry
import swapper
from django.conf import settings


class Industry(BaseIndustry):
    class Meta:
        db_table = 'accelerator_industry'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        verbose_name_plural = "Industries"
        swappable = swapper.swappable_setting('accelerator',
                                              'Industry')

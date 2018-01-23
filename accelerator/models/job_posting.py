# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper
from accelerator_abstract.models import BaseJobPosting
from django.conf import settings


class JobPosting(BaseJobPosting):
    class Meta:
        db_table = 'accelerator_jobposting'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        verbose_name_plural = 'Job postings for startups'
        app_label = 'accelerator'
        swappable = swapper.swappable_setting(app_label,
                                              'JobPosting')

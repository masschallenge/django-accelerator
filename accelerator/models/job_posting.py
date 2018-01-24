# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper
from accelerator_abstract.models import BaseJobPosting
from django.conf import settings


class JobPosting(BaseJobPosting):
    class Meta(BaseJobPosting.Meta):
        swappable = swapper.swappable_setting(BaseJobPosting.Meta.app_label,
                                              'JobPosting')

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper
from accelerator_abstract.models import BaseRecommendationTag
from django.conf import settings


class RecommendationTag(BaseRecommendationTag):
    class Meta:
        db_table = 'accelerator_recommendationtag'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        swappable = swapper.swappable_setting('accelerator',
                                              'RecommendationTag')

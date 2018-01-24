# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper
from accelerator_abstract.models import BaseRecommendationTag
from django.conf import settings


class RecommendationTag(BaseRecommendationTag):
    class Meta(BaseRecommendationTag.Meta):
        swappable = swapper.swappable_setting(
            BaseRecommendationTag.Meta.app_label, 'RecommendationTag')

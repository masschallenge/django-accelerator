# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseRecommendationTag(AcceleratorModel):
    """
    Tag model used for storing keywords for a particular model.
    This is also fed into the recommendation engine.
    """
    text = models.TextField()

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_recommendationtag'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        abstract = True

    def __str__(self):
        return "Recommendation Tag: {}".format(self.text)

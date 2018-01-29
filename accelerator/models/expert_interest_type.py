# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models import BaseExpertInterestType


class ExpertInterestType(BaseExpertInterestType):
    """A category of involvement an expert has with a program or program family
    """
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=255)

    class Meta(BaseExpertInterestType.Meta):
        swappable = swapper.swappable_setting(
            BaseExpertInterestType.Meta.app_label, "ExpertInterestType")
        abstract = True
        verbose_name_plural = "Expert Interest Types"

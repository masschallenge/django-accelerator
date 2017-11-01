# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper
from accelerator_abstract.models import (
    BaseStartup,
    DEFAULT_PROFILE_BACKGROUND_COLOR,
    DEFAULT_PROFILE_TEXT_COLOR,
    STARTUP_COMMUNITIES,
)
from django.conf import settings


class Startup(BaseStartup):
    class Meta:
        db_table = 'accelerator_startup'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        verbose_name_plural = "Startups"
        ordering = ["organization__name"]
        swappable = swapper.swappable_setting('accelerator',
                                              'Startup')

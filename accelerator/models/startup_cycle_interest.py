# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db.models import (
    ForeignKey,
    ManyToManyField,
)

from accelerator_abstract.models.base_startup_cycle_interest import BaseStartupCycleInterest


class StartupCycleInterest(BaseStartupCycleInterest):
    class Meta(BaseStartupCycleInterest.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupCycleInterest.Meta.app_label, "StartupCycleInterest")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
from ordered_model.models import OrderedModel
import logging

from accelerator_abstract.models.base_startup_program_interest import BaseStartupProgramInterest


class StartupProgramInterest(BaseStartupProgramInterest):
    class Meta(BaseStartupProgramInterest.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupProgramInterest.Meta.app_label,
            "StartupProgramInterest")

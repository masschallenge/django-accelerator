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

logger = logging.getLogger(__file__)

INTEREST_CHOICES = [
    ("g", "Definitely will participate"),
    ("w", "Will participate"),
    ("p", "Likely will participate"),
    ("n", "Might not participate"),
    ("l", "Likely won't participate"),
]
PROGRAM_INTEREST_BOTTOM = 'bottom'
PROGRAM_INTEREST_TOP = 'top'
PROGRAM_INTEREST_UP = 'up'
PROGRAM_INTEREST_DOWN = 'down'


@python_2_unicode_compatible
class BaseStartupProgramInterest(OrderedModel, AcceleratorModel):
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"))
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"))
    startup_cycle_interest = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "StartupCycleInterest"),
        blank=True,
        null=True)
    order_with_respect_to = 'startup_cycle_interest'
    applying = models.BooleanField(default=False)
    interest_level = models.CharField(
        max_length=64,
        choices=INTEREST_CHOICES,
        blank=True,
        null=True
    )

    class Meta(OrderedModel.Meta, AcceleratorModel.Meta):
        ordering = ['order']
        abstract = True
        db_table = '{}_startuporograminterest'.format(
            AcceleratorModel.Meta.app_label)

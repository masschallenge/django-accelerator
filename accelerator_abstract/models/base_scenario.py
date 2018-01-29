# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.conf import settings
from django.db import models

DEFAULT_PANEL_SIZE = 10


@python_2_unicode_compatible
class BaseScenario(AcceleratorModel):
    name = models.CharField(max_length=40)
    judging_round = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgingRound"), blank=True, null=True)
    description = models.TextField(max_length=512, blank=True)
    judges = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="scenarios",
        through="ScenarioJudge")
    applications = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Application'),
        related_name="scenarios",
        through="ScenarioApplication")
    # Default False and set True when selected. Only one may be True.
    is_active = models.BooleanField(default=False)
    panel_size = models.IntegerField(blank=True,
                                     default=DEFAULT_PANEL_SIZE,
                                     null=False)
    max_panels_per_judge = models.IntegerField(blank=True, null=True)
    min_panels_per_judge = models.IntegerField(blank=True,
                                               default=0,
                                               null=False)
    sequence_number = models.PositiveIntegerField(
        help_text="Indicate the order for this scenario within the round",
        blank=True,
        null=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_scenario'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        return self.name

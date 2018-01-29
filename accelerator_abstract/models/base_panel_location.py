# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel

@python_2_unicode_compatible
class BasePanelLocation(AcceleratorModel):
    location = models.CharField(max_length=225, primary_key=True)
    description = models.CharField(max_length=225)
    judging_round = models.ForeignKey(swapper.get_model_name(
        'accelerator', 'JudgingRound'), blank=True, null=True)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Panel Locations'
        ordering = ['judging_round', 'description']
        abstract = True
        db_table = '{}_program'.format(AcceleratorModel.Meta.app_label)

    def __str__(self):
        return self.description

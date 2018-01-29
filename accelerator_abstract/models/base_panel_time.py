# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BasePanelTime(AcceleratorModel):
    day = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    start_date_time = models.DateTimeField(blank=False, null=True)
    end_date_time = models.DateTimeField(blank=False, null=True)
    judging_round = models.ForeignKey(swapper.get_model_name(
        'accelerator', 'JudgingRound'), blank=True, null=True)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Panel Times'
        ordering = ['judging_round', 'start_date_time']
        abstract = True
        db_table = '{}_paneltime'.format(AcceleratorModel.Meta.app_label)

    def __str__(self):
        return self.create_time_frame(self.start_date_time)

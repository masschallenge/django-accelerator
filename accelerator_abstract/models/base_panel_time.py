# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.utils import (
    HOUR_FORMAT,
    local_time,
)


@python_2_unicode_compatible
class BasePanelTime(AcceleratorModel):
    day = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    start_date_time = models.DateTimeField(blank=False, null=True)
    end_date_time = models.DateTimeField(blank=False, null=True)
    judging_round = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, 'JudgingRound'),
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Panel Times'
        ordering = ['judging_round', 'start_date_time']
        abstract = True
        db_table = 'accelerator_paneltime'

    def __str__(self):
        return self.create_time_frame(self.start_date_time)

    def create_time_frame(self, start_time):
        return u"%s, %s-%s" % (
            self.day,
            local_time(start_time).strftime(HOUR_FORMAT),
            local_time(self.end_date_time).strftime(HOUR_FORMAT))

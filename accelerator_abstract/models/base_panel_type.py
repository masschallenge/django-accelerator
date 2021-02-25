# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BasePanelType(AcceleratorModel):
    panel_type = models.CharField(max_length=225, primary_key=True)
    description = models.CharField(max_length=225)
    judging_round = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, 'JudgingRound'),
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Panel Types'
        ordering = ['judging_round', 'description']
        abstract = True
        db_table = 'accelerator_paneltype'

    def __str__(self):
        return self.description

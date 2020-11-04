# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

JUDGE_AVAILABILITY_AVAILABLE = "Available"
JUDGE_AVAILABILITY_NOT_AVAILABLE = "Not Available"
JUDGE_AVAILABILITY_PREFERRED = "Preferred"

JUDGE_AVAILABILITY_CHOICES = (
    (JUDGE_AVAILABILITY_AVAILABLE, JUDGE_AVAILABILITY_AVAILABLE),
    (JUDGE_AVAILABILITY_NOT_AVAILABLE, JUDGE_AVAILABILITY_NOT_AVAILABLE),
    (JUDGE_AVAILABILITY_PREFERRED, JUDGE_AVAILABILITY_PREFERRED),
)


class BaseJudgeAvailability(AcceleratorModel):
    commitment = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgeRoundCommitment"),
        on_delete=models.CASCADE)
    panel_location = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "PanelLocation"),
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    panel_time = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "PanelTime"),
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    panel_type = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "PanelType"),
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    availability_type = models.CharField(
        max_length=32,
        choices=JUDGE_AVAILABILITY_CHOICES)

    # vocabularies for type time and location must be drawn from entries
    # consistent with the round associated with the chosen 'commitment'
    # object.
    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_judgeavailability'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = ("Judge availability for specific Panel types, "
                               "times, locations")
        unique_together = ('commitment', 'panel_location', 'panel_time',
                           'panel_type')
        ordering = ['panel_time__start_date_time', 'panel_type__panel_type',
                    'panel_location__location']

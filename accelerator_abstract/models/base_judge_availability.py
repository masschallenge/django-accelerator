# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseJudgeAvailability(AcceleratorModel):
    commitment = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgeRoundCommitment"))
    panel_location = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "PanelLocation"), blank=True, null=True)
    panel_time = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "PanelTime"), blank=True, null=True)
    panel_type = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "PanelType"),
        blank=True, null=True)
    availability_type = models.CharField(
        max_length=32,
        choices=(("Preferred", "Preferred"), ("Available", "Available"),
                 ("Not Available", "Not Available"))
    )

    # vocabularies for type time and location must be drawn from entries
    # consistent with the round associated with the chosen 'commitment'
    # object.
    class Meta(AcceleratorModel.Meta):
        db_table = '{}_judgeavailability'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = ("Judge availability for specific Panel types, "
                               "times, locations")
        unique_together = ('commitment', 'panel_location', 'panel_time',
                           'panel_type')
        ordering = ['panel_time__start_date_time', 'panel_type__panel_type',
                    'panel_location__location']

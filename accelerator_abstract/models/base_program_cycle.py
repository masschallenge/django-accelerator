# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

NAME_AS_PROGRAM_FAMILIES_AND_YEAR = "{relevant_program_families} {year}"


@python_2_unicode_compatible
class BaseProgramCycle(AcceleratorModel):
    """Association of relatively simultaneous programs"""
    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=32, blank=True, null=True)
    applications_open = models.BooleanField(default=False)
    application_open_date = models.DateTimeField(blank=True, null=True)
    application_early_deadline_date = models.DateTimeField(
        blank=True,
        null=True)
    application_final_deadline_date = models.DateTimeField(
        blank=True,
        null=True)
    advertised_final_deadline = models.DateTimeField(
        blank=True,
        null=True)
    accepting_references = models.BooleanField(default=False)
    default_application_type = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ApplicationType"),
        null=True,
        blank=True,
        related_name="application_type_for")
    default_overview_application_type = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ApplicationType"),
        null=True,
        blank=True,
        related_name="default_overview_application_type_for")
    hidden = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = "program cycles"
        db_table = '{}_programcycle'.format(AcceleratorModel.Meta.app_label)
        abstract = True


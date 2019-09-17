# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.core.exceptions import ValidationError
from django.db import models


from accelerator_abstract.models.accelerator_model import AcceleratorModel

NAME_AS_PROGRAM_FAMILIES_AND_YEAR = "{relevant_program_families} {year}"


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
    fields = '__all__'

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = "program cycles"
        db_table = '{}_programcycle'.format(AcceleratorModel.Meta.app_label)
        abstract = True

    def clean(self):
        if (self.applications_open is True and
                not self.default_application_type):
            raise ValidationError(
                'Open applications must have a default '
                ' application type.')

        if (not self.default_application_type and
                self.programs.exists() and
                self.applications_open is True):
            raise ValidationError(
                'The program cycle is associated with '
                ' and the default application type can’t '
                ' be removed from the cycle until the program'
                ' cycle is disassociated with all programs')

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

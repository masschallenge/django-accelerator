# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import decimal

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseProgramOverride(AcceleratorModel):
    cycle = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramCycle"),
        blank=True,
        null=True,
        related_name='program_overrides',
        on_delete=models.CASCADE)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'Program'),
        on_delete=models.CASCADE)
    # this field will be removed after data migration
    name = models.CharField(max_length=50)
    applications_open = models.BooleanField(default=False)
    application_open_date = models.DateTimeField(blank=True, null=True)
    application_early_deadline_date = models.DateTimeField(blank=True,
                                                           null=True)
    application_final_deadline_date = models.DateTimeField(blank=True,
                                                           null=True)
    early_application_fee = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=decimal.Decimal('0.00'),
    )
    regular_application_fee = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=decimal.Decimal('0.00'),
    )

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_programoverride'
        abstract = True
        verbose_name_plural = 'Program Overrides'

    def __str__(self):
        return "Program override (%s) for %s" % (self.name, self.program.name)

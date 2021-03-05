# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseInterestCategory(AcceleratorModel):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=500, blank=True)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_interestcategory'
        abstract = True
        verbose_name_plural = "Interest Categories"

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseApplicationType(AcceleratorModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    submission_label = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, 'StartupLabel'),
        null=True, blank=True)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Application Types'
        db_table = '{}_applicationtype'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

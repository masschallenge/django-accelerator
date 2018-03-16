# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseJudgingForm(AcceleratorModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_judgingform'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Judging Forms'

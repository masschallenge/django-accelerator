# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.label_model import LabelModel


@python_2_unicode_compatible
class BaseStartupLabel(LabelModel):
    label = models.CharField(max_length=LabelModel.LABEL_LENGTH)
    startups = models.ManyToManyField(
        swapper.get_model_name(LabelModel.Meta.app_label, 'Startup'),
        blank=True)

    class Meta(LabelModel.Meta):
        ordering = ['label', ]
        db_table = 'accelerator_startuplabel'
        abstract = True

    def __str__(self):
        return self.label

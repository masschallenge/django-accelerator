# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.label_model import LabelModel


@python_2_unicode_compatible
class BaseNamedGroup(LabelModel):
    name = models.CharField(max_length=LabelModel.LABEL_LENGTH, default='')

    class Meta(LabelModel.Meta):
        ordering = ['name']
        db_table = '{}_namedgroup'.format(LabelModel.Meta.app_label)
        abstract = True


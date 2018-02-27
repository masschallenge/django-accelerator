# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.label_model import LabelModel


@python_2_unicode_compatible
class BaseUserLabel(LabelModel):
    label = models.CharField(max_length=LabelModel.LABEL_LENGTH)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    class Meta(LabelModel.Meta):
        db_table = '{}_userlabel'.format(
            LabelModel.Meta.app_label)
        abstract = True
        ordering = ["label", ]

    def __str__(self):
        return self.label

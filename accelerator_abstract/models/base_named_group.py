# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from accelerator_abstract.models.label_model import LabelModel


@python_2_unicode_compatible
class BaseNamedGroup(LabelModel):
    name = models.CharField(max_length=LabelModel.LABEL_LENGTH, default="")

    class Meta(LabelModel.Meta):
        ordering = ["name"]
        db_table = "accelerator_namedgroup"
        abstract = True

    def __str__(self):
        return self.name

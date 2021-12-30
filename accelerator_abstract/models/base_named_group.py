from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.label_model import LabelModel


class BaseNamedGroup(LabelModel):
    name = models.CharField(max_length=LabelModel.LABEL_LENGTH, default='')

    class Meta(LabelModel.Meta):
        ordering = ['name']
        db_table = 'accelerator_namedgroup'
        abstract = True

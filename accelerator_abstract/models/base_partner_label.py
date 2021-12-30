from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.label_model import LabelModel


class BasePartnerLabel(LabelModel):
    label = models.CharField(max_length=LabelModel.LABEL_LENGTH)
    partners = models.ManyToManyField(
        swapper.get_model_name(LabelModel.Meta.app_label, 'Partner'),
        blank=True)

    class Meta(LabelModel.Meta):
        ordering = ['label', ]
        db_table = 'accelerator_partnerlabel'
        abstract = True

    def __str__(self):
        return self.label

from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from accelerator_abstract.models.label_model import LabelModel

JUDGING_ROUND_FORMAT = "{judging_round} {state} Judge"
DESIRED_JUDGE_STATE = "Desired"
CONFIRMED_JUDGE_STATE = "Confirmed"


class BaseUserLabel(LabelModel):
    label = models.CharField(max_length=LabelModel.LABEL_LENGTH)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    class Meta(LabelModel.Meta):
        db_table = 'accelerator_userlabel'
        abstract = True
        ordering = ["label", ]

    def __str__(self):
        return self.label

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

MIGRATION_STATUS_OLD = "OLD"
MIGRATION_STATUS_MIGRATING = "MIGRATING"
MIGRATION_STATUS_DONE = "DONE"
MIGRATION_STATUS_ERROR = "ERROR"

MODEL_CHANGE_STATUSES = [
    MIGRATION_STATUS_OLD,
    MIGRATION_STATUS_MIGRATING,
    MIGRATION_STATUS_DONE,
    MIGRATION_STATUS_ERROR,
]

MODEL_CHANGE_STATUS_CHOICES = [(x, x) for x in MODEL_CHANGE_STATUSES]


@python_2_unicode_compatible
class BaseModelChange(AcceleratorModel):
    name = models.CharField(max_length=128, unique=True)
    status = models.CharField(max_length=64,
                              choices=MODEL_CHANGE_STATUS_CHOICES,
                              default=MIGRATION_STATUS_OLD)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_modelchange'.format(AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        return "{} ({})".format(self.name, self.status)

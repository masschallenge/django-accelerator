# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseCurrency(AcceleratorModel):
    name = models.CharField(max_length=64, unique=True)
    abbr = models.CharField(max_length=3, unique=True)
    usd_exchange = models.FloatField()

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_currency'.format(AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        return self.name

from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseCurrency(AcceleratorModel):
    name = models.CharField(max_length=64, unique=True)
    abbr = models.CharField(max_length=3, unique=True)
    usd_exchange = models.FloatField()

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_currency'
        abstract = True

from django.conf import settings
from django.db import models

from accelerator.models.accelerator_model import AcceleratorModel


class Currency(AcceleratorModel):
    name = models.CharField(max_length=64, unique=True)
    abbr = models.CharField(max_length=3, unique=True)
    usd_exchange = models.FloatField()

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_currency'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED

    def __str__(self):
        return self.name

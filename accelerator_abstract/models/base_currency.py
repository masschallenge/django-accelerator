# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseCurrency(AcceleratorModel):
    name = models.CharField(max_length=64, unique=True)
    abbr = models.CharField(max_length=3, unique=True)
    usd_exchange = models.FloatField()

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_currency'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        abstract = True

    def __str__(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(c["id"], c["name"])
                for c in cls.objects.all().values("id", "name")]

    @classmethod
    def default_currency(cls):
        usd = cls.objects.filter(abbr="USD")
        if usd:
            return usd[0]
        return cls.objects.all()[0]

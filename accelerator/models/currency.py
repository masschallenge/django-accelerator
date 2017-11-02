# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.conf import settings
from accelerator_abstract.models import BaseCurrency
import swapper


class Currency(BaseCurrency):
    class Meta:
        db_table = 'accelerator_currency'
        app_label = 'accelerator'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        swappable = swapper.swappable_setting(app_label,
                                              'Currency')

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

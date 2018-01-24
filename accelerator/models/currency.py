# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from accelerator_abstract.models import BaseCurrency
import swapper


class Currency(BaseCurrency):
    class Meta(BaseCurrency.Meta):
        swappable = swapper.swappable_setting(BaseCurrency.Meta.app_label,
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

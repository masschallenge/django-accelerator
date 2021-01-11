# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_currency import BaseCurrency


class Currency(BaseCurrency):

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

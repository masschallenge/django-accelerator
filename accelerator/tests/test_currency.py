# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from accelerator.models import Currency
from .factories.currency_factory import CurrencyFactory


class TestCurrency(TestCase):
    def test_currency(self):
        CurrencyFactory(name="US Dollars",
                        abbr="USD")
        assert Currency.objects.get(abbr="USD")

    def test_usd_default(self):
        CurrencyFactory(abbr="GBP")
        usd_name = "US Dollars"
        cur_usd = CurrencyFactory(abbr="USD", name=usd_name)
        assert cur_usd == Currency.default_currency()
        assert usd_name in str(cur_usd)

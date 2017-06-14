from django.test import TestCase
from accelerator.models import Currency
from .factories.currency_factory import CurrencyFactory


class TestCurrency(TestCase):

    def test_currency(self):
        CurrencyFactory(name="US Dollars",
                        abbr="USD")
        assert Currency.objects.get(abbr="USD")

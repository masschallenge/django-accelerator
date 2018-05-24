from django.test import TestCase

from accelerator.tests.factories import LegalCheckFactory


class TestLegalCheck(TestCase):

    def test_str(self):
        legal_check = LegalCheckFactory()
        assert legal_check.name in str(legal_check)

from django.test import TestCase

from accelerator.tests.factories import LegalCheckFactory


class TestLegalCheck(TestCase):
    legal_check = LegalCheckFactory()
    assert legal_check.title in str(legal_check)

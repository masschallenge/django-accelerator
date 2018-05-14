from django.test import TestCase

from accelerator.tests.factories import LegalCheckAcceptanceFactory


class TestLegalCheckAcceptance(TestCase):
    legal_check_acceptance = LegalCheckAcceptanceFactory()
    assert legal_check_acceptance.legal_check.title in str(
        legal_check_acceptance)

from django.test import TestCase

from accelerator.tests.factories import UserLegalCheckFactory


class TestUserLegalCheck(TestCase):
    user_legal_check = UserLegalCheckFactory()
    assert user_legal_check.legal_check.title in str(user_legal_check)

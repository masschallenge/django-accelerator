from django.test import TestCase

from accelerator.tests.factories import UserLegalCheckFactory


class TestUserLegalCheck(TestCase):
    def test_str(self):
        user_legal_check = UserLegalCheckFactory()
        assert user_legal_check.legal_check.name in str(user_legal_check)

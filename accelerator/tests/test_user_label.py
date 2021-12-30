from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import UserLabelFactory


class TestUserLabel(TestCase):
    def test_str(self):
        user_label = UserLabelFactory()
        assert user_label.label in str(user_label)

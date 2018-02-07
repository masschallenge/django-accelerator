# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories import UserRoleFactory


class TestUserRole(TestCase):

    def test_str(self):
        user_role = UserRoleFactory()
        self.assertEqual(str(user_role), user_role.name)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories.user_role_factory import UserRoleFactory


class TestUserRole(TestCase):

    def test_create(self):
        user_role = UserRoleFactory()
        self.assertTrue("User Role" in user_role.name)

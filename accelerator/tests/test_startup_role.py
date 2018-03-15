# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import StartupRoleFactory


class TestStartupRole(TestCase):
    def test_str(self):
        startup_role = StartupRoleFactory()
        assert startup_role.name in str(startup_role)

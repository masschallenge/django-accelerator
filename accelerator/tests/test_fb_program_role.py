# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories.program_role_factory import ProgramRoleFactory


class TestProgramRole(TestCase):

    def test_create(self):
        role = ProgramRoleFactory()
        self.assertTrue("Program Role" in role.name)

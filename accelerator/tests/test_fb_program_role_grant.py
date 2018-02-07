# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories.program_role_grant_factory import ProgramRoleGrantFactory


class TestProgramRoleGrant(TestCase):

    def test_create(self):
        role = ProgramRoleGrantFactory()
        self.assertTrue(role.person.get_profile().current_program !=
                        role.program_role.program)

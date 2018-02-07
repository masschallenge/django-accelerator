# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories.program_family_factory import ProgramFamilyFactory


class TestProgramFamily(TestCase):

    def test_create(self):
        family = ProgramFamilyFactory()
        self.assertTrue("Program Family" in family.name)

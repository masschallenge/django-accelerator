# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories.program_factory import ProgramFactory


class TestProgram(TestCase):

    def test_create(self):
        program = ProgramFactory()
        self.assertTrue("Program" in program.name)

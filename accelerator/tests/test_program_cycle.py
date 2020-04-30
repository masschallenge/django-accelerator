# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase

from accelerator.tests.factories import ProgramCycleFactory


class TestProgramCycle(TestCase):
    def test_program_cycle_requires_default_application_type(self):
        with self.assertRaises(ValidationError):
            ProgramCycleFactory(default_application_type=None,
                                applications_open=True)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from accelerator.tests.factories import ProgramCycleFactory


class TestProgramCycle(TestCase):
    def test_program_cycle_requires_short_name(self):
        with self.assertRaises(IntegrityError):
            ProgramCycleFactory(short_name=None)

    def test_program_cycle_requires_default_application_type(self):
        with self.assertRaises(ValidationError):
            ProgramCycleFactory(default_application_type=None,
                                applications_open=True)

    def test_program_cycle_requires_advertised_final_deadline(self):
        with self.assertRaises(IntegrityError):
            ProgramCycleFactory(advertised_final_deadline=None)

    def test_program_cycle_requires_application_open_date(self):
        with self.assertRaises(IntegrityError):
            ProgramCycleFactory(application_open_date=None)

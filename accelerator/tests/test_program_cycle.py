# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase


from accelerator.tests.factories import ProgramCycleFactory


class TestProgramCycle(TestCase):
    def test_display_name_no_short_name(self):
        cycle = ProgramCycleFactory(short_name=None)
        assert cycle.name in str(cycle)

    def test_program_cycle_has_default_application_type(self):
        cycle = ProgramCycleFactory(default_application_type=None,
                                    applications_open=True)
        try:
            cycle.full_clean()
        except ValidationError as e:
            self.assertRaises(e)

    def test_program_cycle_cannot_remove_default_application_type(self):
        cycle = ProgramCycleFactory(default_application_type=None,
                                    applications_open=True)
        if (cycle.programs.exists()):
            try:
                cycle.full_clean()
            except ValidationError as e:
                self.assertRaises(e)

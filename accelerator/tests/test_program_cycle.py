# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ProgramCycleFactory


class TestProgramCycle(TestCase):
    def test_display_name_no_short_name(self):
        cycle = ProgramCycleFactory(short_name=None)
        assert cycle.name in str(cycle)

    def test_program_cycle_has_default_application_type(self):
        cycle = ProgramCycleFactory()
        if (cycle.applications_open and
                not cycle.default_application_type):
            self.assertRaises("Open applications must have"
                              "a default application type.")

    def test_program_cycle_cannot_remove_default_application_type(self):
        cycle = ProgramCycleFactory()
        if (cycle.applications_open and
                not cycle.default_application_type
                and cycle.programs.exists()):
            self.assertRaises("Default application type can’t be removed"
                              "from the cycle until the program cycle is"
                              "disassociated with all programs")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ProgramCycleFactory


class TestProgramCycle(TestCase):
    def test_display_name_no_short_name(self):
        cycle = ProgramCycleFactory(short_name=None)
        assert cycle.name in str(cycle)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ProgramOverrideFactory


class TestProgramOverride(TestCase):

    def test_str(self):
        program_override = ProgramOverrideFactory()
        assert program_override.name in str(program_override)
        assert program_override.program.name in str(program_override)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from accelerator.tests.factories import (
    ProgramFactory,
    ProgramFamilyFactory,
)


class TestProgram(TestCase):
    def test_str(self):
        program = ProgramFactory()
        assert program.name in str(program)

    def test_family_abbr(self):
        lower_case_slug = 'foo bar'  # we do not enforce slugs
        program_family = ProgramFamilyFactory(url_slug=lower_case_slug)
        program = ProgramFactory(program_family=program_family)
        self.assertEqual(lower_case_slug.upper(),
                         program.family_abbr())

    def test_program_requires_end_date(self):
        with self.assertRaises(IntegrityError):
            ProgramFactory(end_date=None)

    def test_program_requires_location(self):
        with self.assertRaises(IntegrityError):
            ProgramFactory(location=None)

    def test_program_requires_start_date(self):
        with self.assertRaises(IntegrityError):
            ProgramFactory(start_date=None)

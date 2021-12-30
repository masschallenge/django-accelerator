from __future__ import unicode_literals

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

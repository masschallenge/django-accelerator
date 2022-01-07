from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ProgramStartupAttributeFactory


class TestProgramStartupAttribute(TestCase):

    def test_str(self):
        program_startup_attribute = ProgramStartupAttributeFactory()
        assert program_startup_attribute.attribute_label in str(
            program_startup_attribute)
        assert 'Text Line' in str(program_startup_attribute)

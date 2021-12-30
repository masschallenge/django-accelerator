from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import SectionFactory


class TestSection(TestCase):

    def test_str(self):
        section = SectionFactory()
        assert section.heading in str(section)

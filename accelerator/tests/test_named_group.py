from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import NamedGroupFactory


class TestNamedGroup(TestCase):
    def test_str(self):
        group = NamedGroupFactory()
        assert group.name in str(group)

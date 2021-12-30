from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import FunctionalExpertiseFactory


class TestFunctionalExpertise(TestCase):

    def test_str(self):
        parent_functional_expertise = FunctionalExpertiseFactory()
        functional_expertise = FunctionalExpertiseFactory(
            parent=parent_functional_expertise)
        assert functional_expertise.name in str(functional_expertise)
        assert parent_functional_expertise.name in str(functional_expertise)

    def test_add_parent(self):
        parent = FunctionalExpertiseFactory()
        child = FunctionalExpertiseFactory(parent=parent)
        self.assertEqual(child.parent, parent)

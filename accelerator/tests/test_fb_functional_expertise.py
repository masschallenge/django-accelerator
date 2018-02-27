# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories.functional_expertise_factory import (
    FunctionalExpertiseFactory
)


class TestFunctionalExpertise(TestCase):

    def test_create(self):
        expertise = FunctionalExpertiseFactory()
        self.assertTrue("Functional Expertise" in expertise.name)

    def test_add_parent(self):
        parent = FunctionalExpertiseFactory()
        child = FunctionalExpertiseFactory(parent=parent)
        self.assertEqual(child.parent, parent)

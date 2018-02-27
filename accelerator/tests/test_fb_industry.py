# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories.industry_factory import IndustryFactory


class TestIndustry(TestCase):

    def test_create(self):
        industry = IndustryFactory()
        self.assertTrue("Industry" in industry.name)

    def test_add_parent(self):
        parent = IndustryFactory()
        child = IndustryFactory(parent=parent)
        self.assertEqual(child.parent, parent)

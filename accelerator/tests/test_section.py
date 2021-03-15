# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.accelerator.tests.factories import SectionFactory


class TestSection(TestCase):

    def test_str(self):
        section = SectionFactory()
        assert section.heading in str(section)

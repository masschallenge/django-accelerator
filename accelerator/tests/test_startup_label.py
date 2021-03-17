# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import StartupLabelFactory


class TestStartupLabel(TestCase):
    def test_str(self):
        label = StartupLabelFactory()
        assert label.label in str(label)

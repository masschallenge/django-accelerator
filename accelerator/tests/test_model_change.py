# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ModelChangeFactory


class TestModelChange(TestCase):

    def test_str(self):
        model_change = ModelChangeFactory()
        assert str(model_change.name) in str(model_change)
        assert str(model_change.status) in str(model_change)

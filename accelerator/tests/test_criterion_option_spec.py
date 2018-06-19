# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from .factories import (
    CriterionOptionSpecFactory
)


class TestCriterionOptionSpec(TestCase):

    def test_str(self):
        spec = CriterionOptionSpecFactory()
        assert spec.option in str(spec)

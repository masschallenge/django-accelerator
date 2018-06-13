# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from .factories import (
    CriterionFactory
)


class TestCriterion(TestCase):

    def test_str(self):
        criterion = CriterionFactory
        assert bucket_state.name in str(bucket_state)

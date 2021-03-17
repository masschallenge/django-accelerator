# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ReferenceFactory
from accelerator.tests.utils import days_from_now


class TestReference(TestCase):

    def test_str_for_unsubmitted_request(self):
        obj = ReferenceFactory(submitted=None)
        name = str(obj)
        assert str(obj.application) in name
        assert str(obj.email) in name
        assert " request " in name

    def test_str_for_submitted_request(self):
        obj = ReferenceFactory(submitted=days_from_now(-1))
        name = str(obj)
        assert str(obj.application) in name
        assert str(obj.email) in name
        assert " request " not in name

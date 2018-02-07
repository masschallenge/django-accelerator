# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    ExpertFactory,
)


class TestCoreProfile(TestCase):
    def test_full_name(self):
        user = ExpertFactory(first_name="", last_name="")
        assert user.get_profile().full_name() == str(user.username)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import BaseProfileFactory


class TestBaseProfile(TestCase):

    def test_create(self):
        profile = BaseProfileFactory()
        self.assertEqual("ENTREPRENEUR", profile.user_type)
        self.assertEqual(True, profile.user.is_active)

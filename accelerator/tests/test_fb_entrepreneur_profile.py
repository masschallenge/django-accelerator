# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories.entrepreneur_profile_factory import EntrepreneurProfileFactory
from accelerator.tests.factories.recommendation_tag_factory import RecommendationTagFactory


class TestEntrepreneurProfile(TestCase):

    def test_create(self):
        profile = EntrepreneurProfileFactory()
        self.assertEqual(True, profile.user.is_active)
        self.assertTrue("" != profile.bio)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories.recommendation_tag_factory import RecommendationTagFactory


class TestRecommendationTag(TestCase):

    def test_create(self):
        tag = RecommendationTagFactory()
        self.assertTrue("tag_" in tag.text)

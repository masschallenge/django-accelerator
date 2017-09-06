# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from .factories.recommendation_tag_factory import RecommendationTagFactory


class TestRecommendationTag(TestCase):
    def test_recommendation_tag(self):
        tag = RecommendationTagFactory()
        self.assertTrue(tag.text in str(tag))

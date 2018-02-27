# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.models import VALID_EXPERT_CATEGORIES
from accelerator.tests.factories.expert_category_factory import (
    ExpertCategoryFactory
)


class TestExpertCategory(TestCase):

    def test_create(self):
        category = ExpertCategoryFactory()
        self.assertTrue(category.name in VALID_EXPERT_CATEGORIES)

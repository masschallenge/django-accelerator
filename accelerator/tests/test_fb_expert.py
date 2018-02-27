# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator_abstract.models.base_user_utils import (
    is_entrepreneur,
    is_expert,
    is_member,
)


class TestExpert(TestCase):

    def test_create(self):
        user = ExpertFactory()
        self.assertFalse(is_entrepreneur(user))
        self.assertTrue(is_expert(user))
        self.assertFalse(is_member(user))

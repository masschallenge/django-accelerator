# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories.member_factory import MemberFactory
from accelerator_abstract.models.base_user_utils import (
    is_entrepreneur,
    is_expert,
    is_member,
)


class TestMemberProfile(TestCase):

    def test_create(self):
        user = MemberFactory()
        self.assertFalse(is_entrepreneur(user))
        self.assertFalse(is_expert(user))
        self.assertTrue(is_member(user))

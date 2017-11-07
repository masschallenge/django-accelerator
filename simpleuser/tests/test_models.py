# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from .factories.user_factory import UserFactory


class TestUser(TestCase):
    def test_str(self):
        user = UserFactory()
        assert user.email in str(user)


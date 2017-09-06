# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from .factories.user_factory import UserFactory
from django.contrib.auth import get_user_model

User = get_user_model()


class TestUser(TestCase):
    def test_user(self):
        before = User.objects.count()
        User.objects.create_user("user@example.com", "password")
        self.assertEqual(before + 1, User.objects.count())

    def test_user_without_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user()

    def test_superuser(self):
        before = User.objects.filter(is_superuser=True).count()
        User.objects.create_superuser("superuser@example.com", "password")
        self.assertEqual(before + 1,
                         User.objects.filter(is_superuser=True).count())

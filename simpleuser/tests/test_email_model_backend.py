# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase
from .factories.user_factory import UserFactory
from simpleuser.email_model_backend import (
    EmailModelBackend,
    MULTIPLE_USERS_FOUND,
)
User = get_user_model()

BAD_EMAIL = "nosuch@user.com"
BAD_PASSWORD = "bad password"
GOOD_PASSWORD = "good password"


class TestEmailModelBackend(TestCase):
    def test_authenticate_with_email(self):
        backend = EmailModelBackend()
        password = GOOD_PASSWORD
        user = UserFactory(password=make_password(password))
        assert user == backend.authenticate(email=user.email,
                                            password=password)

    def test_authenticate_with_username(self):
        backend = EmailModelBackend()
        password = GOOD_PASSWORD
        user = UserFactory(password=make_password(password))
        assert user == backend.authenticate(username=user.email,
                                            password=password)

    def test_authenticate_with_bad_password(self):
        backend = EmailModelBackend()
        password = GOOD_PASSWORD
        user = UserFactory(password=password)
        assert backend.authenticate(username=user.email,
                                    password=BAD_PASSWORD) is None

    def test_authenticate_with_no_user(self):
        backend = EmailModelBackend()
        assert backend.authenticate(email=BAD_EMAIL,
                                    password=BAD_PASSWORD) is None

    def test_get_user(self):
        backend = EmailModelBackend()
        user = UserFactory()
        assert user == backend.get_user(user.id)

    def test_get_user_for_deleted_user(self):
        backend = EmailModelBackend()
        user = UserFactory()
        id = user.id
        user.delete()
        assert backend.get_user(id) is None

    @patch('simpleuser.email_model_backend.logger')
    def test_authenticate_user_with_duplicated_email(self, mock_logger):
        email = "user@example.com"
        UserFactory(email=email, password="password", username="user1")
        user2 = UserFactory(email=email,
                            password="password",
                            username="user2")
        backend = EmailModelBackend()
        with self.assertRaises(User.AuthenticationException):
            backend.authenticate(user2)
        mock_logger.error.assert_called_with(MULTIPLE_USERS_FOUND % email)

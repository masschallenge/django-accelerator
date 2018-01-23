# MIT License
# Copyright (c) 2017 MassChallenge, Inc.
from mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model
from simpleuser.email_model_backend import (
    EmailModelBackend,
    MULTIPLE_USERS_FOUND,
)
User = get_user_model()


class TestEmailModelBackend(TestCase):

    @patch('simpleuser.email_model_backend.logger')
    def test_multiple_users_with_same_email(self, mock_logger):
        email = "user@example.com"
        User.objects.create(email=email, password="password", username="user1")
        user2 = User.objects.create(email=email,
                                    password="password",
                                    username="user2")
        backend = EmailModelBackend()
        backend.authenticate(user2)
        mock_logger.error.assert_called_with(MULTIPLE_USERS_FOUND % email)

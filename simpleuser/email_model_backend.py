# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.contrib.auth import get_user_model
import logging
logger = logging.getLogger(__name__)

User = get_user_model()

MULTIPLE_USERS_FOUND = "django-accelerator: Multiple users found for email %s"


class EmailModelBackend(object):

    def authenticate(self, email=None, password=None, username=None):
        try:
            if not email:
                email = username
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        except User.MultipleObjectsReturned:
            logger.error(MULTIPLE_USERS_FOUND % email)
            raise User.AuthenticationException
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

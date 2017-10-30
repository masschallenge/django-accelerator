# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves an User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('An email address must be provided.')
        email = self.normalize_email(email)
        if "is_active" not in extra_fields:
            extra_fields["is_active"] = True
        if "username" not in extra_fields:
            extra_fields["username"] = uuid.uuid4()
        user = self.model(email=email,
                          is_staff=is_staff, is_superuser=is_superuser,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractUser):
    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

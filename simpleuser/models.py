# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


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
            # For now we need to have a unique id that is at
            # most 30 characters long.  Using uuid and truncating.
            # Ideally username goes away entirely at some point
            # since we're really using email.  If we have to keep
            # username for some reason then we could switch over
            # to a string version of the pk which is guaranteed
            # be unique.
            extra_fields["username"] = str(uuid.uuid4())[:30]
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


@python_2_unicode_compatible
class User(AbstractUser):
    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.email

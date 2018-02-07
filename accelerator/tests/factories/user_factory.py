# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from factory import (
    DjangoModelFactory,
    Sequence,
)

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda n: "username_{0}".format(n))
    first_name = Sequence(lambda n: "First {0}".format(n))
    last_name = Sequence(lambda n: "Last {0}".format(n))
    email = Sequence(lambda n: "user_{0}@example.com".format(n))
    password = "password"
    is_active = True
    is_staff = False  # Prevent user from accesses /admin by default
    is_superuser = False
    last_login = timezone.now() + timedelta(-1)
    date_joined = (timezone.now() + timedelta(-10)).date()

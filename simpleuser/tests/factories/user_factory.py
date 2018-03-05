# MIT License
# Copyright (c) 2017 MassChallenge, Inc.
from __future__ import unicode_literals

import uuid
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from factory import (
    DjangoModelFactory,
    Sequence,
)

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda n: str(uuid.uuid4())[:30])
    email = Sequence(lambda n: "user_{0}@example.com".format(n))
    first_name = Sequence(lambda n: "First {0}".format(n))
    last_name = Sequence(lambda n: "Last {0}".format(n))
    is_superuser = False
    is_staff = False
    is_active = True
    last_login = timezone.now() + timedelta(-1)
    date_joined = (timezone.now() + timedelta(-10)).date()

    @classmethod
    def _prepare(cls, create, **kwargs):
        # Hash the password if it has been provided
        if 'password' in kwargs:
            kwargs['password'] = make_password(kwargs['password'])
        else:
            kwargs['password'] = make_password('password')

        return super(UserFactory, cls)._prepare(create, **kwargs)

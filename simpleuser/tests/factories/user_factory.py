# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    DjangoModelFactory,
    Sequence,
)

from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User

    username = Sequence(lambda n: "username_{0}".format(n))
    email = Sequence(lambda n: "user_{0}@example.com".format(n))
    first_name = Sequence(lambda n: "First {0}".format(n))
    last_name = Sequence(lambda n: "Last {0}".format(n))
    password = "password"
    is_superuser = False
    is_staff = False
    is_active = True

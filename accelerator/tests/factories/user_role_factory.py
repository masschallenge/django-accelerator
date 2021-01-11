# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import UserRole


class UserRoleFactory(DjangoModelFactory):
    class Meta:
        model = UserRole
        django_get_or_create = ['name']

    name = Sequence(lambda n: "User Role {0}".format(n))
    sort_order = Sequence(lambda n: n)

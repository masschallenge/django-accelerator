# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig

UserRole = swapper.load_model(AcceleratorConfig.name, 'UserRole')


class UserRoleFactory(DjangoModelFactory):
    class Meta:
        model = UserRole

    name = Sequence(lambda n: "User Role {0}".format(n))
    sort_order = Sequence(lambda n: n)

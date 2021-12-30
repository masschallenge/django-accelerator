from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

UserRole = swapper.load_model('accelerator', 'UserRole')


class UserRoleFactory(DjangoModelFactory):
    class Meta:
        model = UserRole
        django_get_or_create = ['name']

    name = Sequence(lambda n: "User Role {0}".format(n))
    sort_order = Sequence(lambda n: n)

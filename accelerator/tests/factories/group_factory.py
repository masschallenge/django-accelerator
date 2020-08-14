# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.contrib.auth.models import Group
from factory import (
    Sequence,
    post_generation,
)
from factory.django import DjangoModelFactory


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = Sequence(lambda n: "test_group{0}".format(n))

    @post_generation
    def permissions(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.permissions.add(tag)

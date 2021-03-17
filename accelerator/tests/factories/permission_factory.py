# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.contrib.auth.models import Permission
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.content_type_factory import ContentTypeFactory


class PermissionFactory(DjangoModelFactory):
    class Meta:
        model = Permission

    name = Sequence(lambda n: "test_permission{0}".format(n))
    content_type = SubFactory(ContentTypeFactory)
    codename = Sequence(lambda n: "test_permcode{0}".format(n))

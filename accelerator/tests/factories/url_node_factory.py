# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from fluent_pages.models import UrlNode

from accelerator.tests.factories import (
    MemberFactory,
)


class UrlNodeFactory(DjangoModelFactory):
    class Meta:
        model = UrlNode

    override_url = Sequence(lambda n: "/node{}/".format(n))
    author = SubFactory(MemberFactory
                        )
    title = Sequence(lambda n: "Url Node {}".format(n))

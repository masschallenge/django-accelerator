# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import NamedGroup


class NamedGroupFactory(DjangoModelFactory):
    name = Sequence(lambda n: "Named Group {0}".format(n))

    class Meta:
        model = NamedGroup

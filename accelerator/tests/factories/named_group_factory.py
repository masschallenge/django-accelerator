# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

NamedGroup = swapper.load_model('accelerator', 'NamedGroup')


class NamedGroupFactory(DjangoModelFactory):
    name = Sequence(lambda n: "Named Group {0}".format(n))

    class Meta:
        model = NamedGroup

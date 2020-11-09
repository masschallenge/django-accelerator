# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

NavTree = swapper.load_model('accelerator', 'NavTree')


class NavTreeFactory(DjangoModelFactory):
    class Meta:
        model = NavTree

    title = Sequence(lambda n: "Tree {0}".format(n))
    alias = Sequence(lambda n: "tree_{0}".format(n))

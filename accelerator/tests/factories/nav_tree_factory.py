# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence
)

from accelerator.apps import AcceleratorConfig

NavTree = swapper.load_model(
    AcceleratorConfig.name, 'NavTree')


class NavTreeFactory(DjangoModelFactory):
    class Meta:
        model = NavTree

    title = Sequence(lambda n: "Tree {0}".format(n))
    alias = Sequence(lambda n: "tree_{0}".format(n))

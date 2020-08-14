# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    SubFactory,
    Sequence
)
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories import (
    NavTreeFactory,
)

NavTreeItem = swapper.load_model(
    AcceleratorConfig.name, 'NavTreeItem')


class NavTreeItemFactory(DjangoModelFactory):
    class Meta:
        model = NavTreeItem
        django_get_or_create = ('tree', 'title', 'url')

    tree = SubFactory(NavTreeFactory)
    title = Sequence(lambda n: "tree item {0}".format(n))
    url = Sequence(lambda n: "/tree_item_{0}".format(n))

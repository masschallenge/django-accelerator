# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories import (
    NavTreeFactory,
    NavTreeItemFactory,
    UrlNodeFactory
)

NodeSideNavAssociation = swapper.load_model(
    AcceleratorConfig.name, 'NodeSideNavAssociation')


class NodeSideNavAssociationFactory(DjangoModelFactory):
    class Meta:
        model = NodeSideNavAssociation
        django_get_or_create = ('node', 'side_nav', 'sub_nav_item')

    node = SubFactory(UrlNodeFactory)
    side_nav = SubFactory(NavTreeFactory)
    sub_nav_item = SubFactory(NavTreeItemFactory)

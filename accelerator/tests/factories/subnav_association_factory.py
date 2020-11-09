# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories import (
    NavTreeFactory,
    NavTreeItemFactory,
    UrlNodeFactory
)

NodeSubNavAssociation = swapper.load_model(
    'accelerator', 'NodeSubNavAssociation')


class NodeSubNavAssociationFactory(DjangoModelFactory):
    class Meta:
        model = NodeSubNavAssociation
        django_get_or_create = ('node', 'sub_nav', 'sub_nav_item')

    node = SubFactory(UrlNodeFactory)
    sub_nav = SubFactory(NavTreeFactory)
    sub_nav_item = SubFactory(NavTreeItemFactory)

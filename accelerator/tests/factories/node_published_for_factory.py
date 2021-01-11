# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_role_factory import ProgramRoleFactory
from accelerator.tests.factories.url_node_factory import UrlNodeFactory

from accelerator.models import NodePublishedFor


class NodePublishedForFactory(DjangoModelFactory):
    class Meta:
        model = NodePublishedFor

    node = SubFactory(UrlNodeFactory)
    published_for = SubFactory(ProgramRoleFactory)

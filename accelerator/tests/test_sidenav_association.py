# MIT License
# Copyright (c) 2019 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import NodeSideNavAssociationFactory


class TestStartupRole(TestCase):
    def test_str(self):
        association = NodeSideNavAssociationFactory()
        assert association.node.title in str(association)
        assert association.sub_nav.title in str(association)

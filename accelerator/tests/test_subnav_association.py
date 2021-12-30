from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import NodeSubNavAssociationFactory


class TestSubNavigation(TestCase):
    def test_str(self):
        association = NodeSubNavAssociationFactory()
        assert association.node.title in str(association)
        assert association.sub_nav.title in str(association)

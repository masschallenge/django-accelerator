# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


from django.test import TestCase

from accelerator.tests.factories import NodePublishedForFactory


class TestNodePublishedFor(TestCase):

    def test_str(self):
        node = NodePublishedForFactory()
        assert node.node.title in str(node)
        assert node.published_for.name in str(node)

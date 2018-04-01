# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import NodePublishedForFactory


class TestNodePublishedFor(TestCase):

    def test_str(self):
        node = NodePublishedForFactory()
        assert node.node.title in str(node)
        assert node.published_for.name in str(node)

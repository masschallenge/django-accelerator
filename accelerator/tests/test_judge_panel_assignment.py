# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from .factories import (
    JudgePanelAssignmentFactory,
)


class TestJudgePanelAssignment(TestCase):

    def test_str(self):
        obj = JudgePanelAssignmentFactory()
        name = str(obj)
        assert str(obj.judge) in name
        assert str(obj.panel) in name

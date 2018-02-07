# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from .factories import (
    StartupMentorRelationshipFactory,
)


class TestStartupMentorRelationship(TestCase):

    def test_str(self):
        obj = StartupMentorRelationshipFactory()
        name = str(obj)
        assert obj.startup_mentor_tracking.startup.name in name
        assert obj.mentor.first_name in name
        assert obj.mentor.last_name in name

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from .factories import (
    StartupMentorTrackingRecordFactory,
)


class TestStartupMentorTrackingRecord(TestCase):

    def test_str(self):
        record = StartupMentorTrackingRecordFactory()
        assert record.startup.name in str(record)

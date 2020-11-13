# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


from django.test import TestCase

from .factories import (
    StartupMentorTrackingRecordFactory,
)


class TestStartupMentorTrackingRecord(TestCase):

    def test_str(self):
        record = StartupMentorTrackingRecordFactory()
        assert record.startup.name in str(record)

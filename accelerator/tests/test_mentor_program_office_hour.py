from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    MentorProgramOfficeHourFactory,
)


class TestMentorProgramOfficeHour(TestCase):
    def test_str(self):
        office_hour = MentorProgramOfficeHourFactory()
        assert office_hour.mentor.email in str(office_hour)

    def test_str_when_open(self):
        office_hour = MentorProgramOfficeHourFactory(finalist=None)
        assert office_hour.mentor.email in str(office_hour)

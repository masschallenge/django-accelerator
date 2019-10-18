from freezegun import freeze_time
from django.test import TestCase

from accelerator.utils import localized_today_utc_date


class TestUtils(TestCase):

    @freeze_time("2019-09-03")
    def test_date_is_localized_to_the_timezone(self):
        self._assert_localized_date_for_timezone_equals(
            "America/New_York",
            "2019-09-03 04:00:00+00:00")

    @freeze_time("2019-09-03")
    def test_date_is_localized_to_the_timezone2(self):
        self._assert_localized_date_for_timezone_equals(
            "Africa/Kampala",
            "2019-09-02 21:00:00+00:00")

    def _assert_localized_date_for_timezone_equals(self, timezone, expected):
        localized_today_date = localized_today_utc_date(timezone)
        self.assertEqual(str(localized_today_date), expected)

from datetime import datetime

import pytz
from django.core.exceptions import ValidationError
from django.db import transaction
from django.test import TestCase

from accelerator_abstract.utils import (
    local_time,
    validate_capacity_options,
)


class TestUtils(TestCase):

    def test_validate_capacity_options(self):
        non_int_value = 'foo'
        val = '5|{}|5'.format(non_int_value)

        with self.assertRaises(ValidationError):
            validate_capacity_options(val)

    @transaction.atomic
    def test_local_time(self):
        local_tz = pytz.timezone('UTC')
        local_morning = local_tz.localize(datetime(2015, 9, 30, 8, 30))
        utc_morning = local_morning.astimezone(pytz.utc)
        assert "AM" == local_time(utc_morning).strftime("%p")

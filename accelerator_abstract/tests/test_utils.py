from django.core.exceptions import ValidationError
from django.test import TestCase

from accelerator_abstract.utils import validate_capacity_options


class TestUtils(TestCase):

    def test_validate_capacity_options(self):
        non_int_value = 'foo'
        val = '5|{}|5'.format(non_int_value)

        with self.assertRaises(ValidationError):
            validate_capacity_options(val)

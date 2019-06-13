from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from accelerator_abstract.models.base_user_utils import (
    is_employee
)
from accelerator.tests.utils import login_as_new_user
from accelerator.tests.factories import (
    ClearanceFactory,
    UserFactory,
)
from accelerator_abstract.models.base_clearance import (
    CLEARANCE_LEVEL_STAFF,
)


class TestBaseUserUtils(TestCase):

    def test_is_employee_for_anonymous_user_is_false(self):
        self.assertFalse(is_employee(AnonymousUser()))

    def test_is_employee_for_superuser_is_true(self):
        user = login_as_new_user(self, UserFactory, is_superuser=True)
        self.assertTrue(is_employee(user))

    def test_is_employee_for_staff_is_true(self):
        user = login_as_new_user(self, UserFactory)
        ClearanceFactory(user=user,
                         level=CLEARANCE_LEVEL_STAFF)
        self.assertTrue(is_employee(user))

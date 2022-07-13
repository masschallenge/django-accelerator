from django.test import TestCase
from accelerator.tests.factories import ClearanceFactory
from mc.models import (
    Clearance,
    CLEARANCE_LEVEL_POM,
    CLEARANCE_LEVEL_GLOBAL_MANAGER
)


class TestClearance(TestCase):

    def test_str(self):
        clearance = ClearanceFactory()
        assert str(clearance.user) in str(clearance)
        assert str(clearance.program_family) in str(clearance)
        assert str(clearance.level) in str(clearance)

    def test_higher_clearance_accepted(self):
        clearance = ClearanceFactory(level=CLEARANCE_LEVEL_GLOBAL_MANAGER)
        user = clearance.user
        cleared = Clearance.objects.check_clearance(user, CLEARANCE_LEVEL_POM)
        self.assertTrue(cleared)

    def test_equal_clearance_accepted(self):
        clearance = ClearanceFactory(level=CLEARANCE_LEVEL_GLOBAL_MANAGER)
        user = clearance.user
        cleared = Clearance.objects.check_clearance(
            user, CLEARANCE_LEVEL_GLOBAL_MANAGER)
        self.assertTrue(cleared)

    def test_lower_clearance_rejected(self):
        clearance = ClearanceFactory(level=CLEARANCE_LEVEL_POM)
        user = clearance.user
        cleared = Clearance.objects.check_clearance(
            user, CLEARANCE_LEVEL_GLOBAL_MANAGER)
        self.assertFalse(cleared)

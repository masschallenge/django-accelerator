from django.test import TestCase

from accelerator.tests.factories import ClearanceFactory


class TestClearance(TestCase):

    def test_str(self):
        clearance = ClearanceFactory()
        assert str(clearance.user) in str(clearance)
        assert str(clearance.program_family) in str(clearance)
        assert str(clearance.level) in str(clearance)


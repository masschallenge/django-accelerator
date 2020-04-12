from django.test import TestCase

from accelerator_abstract.models.base_utils import finalist_startup_member
from accelerator.models.startup_role import StartupRole
from accelerator.tests.contexts import StartupTeamMemberContext


class TestBaseUtils(TestCase):

    def test_finalist_startup_is_true_for_startup_finalist(self):
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=StartupRole.FINALIST)
        self.assertTrue(finalist_startup_member(context.user))

    def test_finalist_startup_is_true_for_startup_non_finalist(self):
        context = StartupTeamMemberContext(primary_contact=False)
        self.assertFalse(finalist_startup_member(context.user))

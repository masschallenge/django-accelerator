from django.test import TestCase

from accelerator_abstract.models.base_utils import (
    finalist_startup_member
)
from accelerator_abstract.models.base_startup_role import (
    BaseStartupRole
)
from accelerator.tests.contexts import (
    StartupTeamMemberContext
)
from accelerator.tests.factories import StartupRoleFactory


class TestBaseUtils(TestCase):

    def test_finalist_startup_is_true_for_startup_finalist(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        self.assertTrue(finalist_startup_member(context.user))

    def test_finalist_startup_is_true_for_startup_non_finalist(self):
        context = StartupTeamMemberContext(primary_contact=False)
        self.assertFalse(finalist_startup_member(context.user))

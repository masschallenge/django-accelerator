from django.test import TestCase

from accelerator.tests.utils import login_as_new_user, login_as_user
from accelerator_abstract.models.base_startup_role import (
    BaseStartupRole
)
from accelerator_abstract.models.base_user_role import (
    BaseUserRole
)
from accelerator.tests.contexts import (
    StartupTeamMemberContext
)
from accelerator.tests.factories import (
    StartupRoleFactory,
    UserFactory
)
from accelerator_abstract.models.base_permission_checks import (
    _see_active_pages,
    _see_employee_pages,
    _see_finalist_pages,
    base_accelerator_check
)
from accelerator_abstract.models import ENDED_PROGRAM_STATUS
from accelerator.tests.test_core_profile import expert


class TestBasePermissionsChecks(TestCase):

    def test_see_employee_pages_is_true_for_staff(self):
        user = login_as_new_user(self, UserFactory, is_superuser=True)
        self.assertTrue(_see_employee_pages(user))

    def test_see_employee_pages_is_false_with_None_argument(self):
        self.assertFalse(_see_employee_pages(None))

    def test_staff_can_see_finalist_pages(self):
        user = login_as_new_user(self, UserFactory, is_superuser=True)
        self.assertTrue(_see_finalist_pages(user))

    def test_finalist_startup_team_member_can_see_finalist_pages(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        login_as_user(self, context.user)
        self.assertTrue(_see_finalist_pages(context.user))

    def test_finalist_in_active_program_can_see_finalist_pages(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        login_as_user(self, context.user)
        self.assertTrue(_see_finalist_pages(context.user))

    def test_finalist_in_active_program_can_see_active_pages(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        login_as_user(self, context.user)
        self.assertTrue(_see_active_pages(context.user))

    def test_mentor_can_see_active_pages(self):
        user = expert(BaseUserRole.MENTOR)
        login_as_user(self, user)
        self.assertTrue(_see_active_pages(user))

    def test_alumni_in_residence_can_see_active_pages(self):
        user = expert(BaseUserRole.AIR)
        login_as_user(self, user)
        self.assertTrue(_see_active_pages(user))

    def test_finalist_in_inactive_program_passes_accelerator_check(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role,
            program_status=ENDED_PROGRAM_STATUS)
        login_as_user(self, context.user)
        self.assertTrue(base_accelerator_check(context.user))

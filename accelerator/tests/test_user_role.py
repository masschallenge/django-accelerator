from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    UserRoleFactory,
    ProgramFactory
)
from accelerator_abstract.models.base_user_role import (
    BaseUserRole,
    is_finalist_user,
    is_judge,
    is_mentor,
)
from accelerator.tests.test_core_profile import expert


class TestUserRole(TestCase):

    def test_str(self):
        user_role = UserRoleFactory()
        self.assertEqual(str(user_role), user_role.name)

    def test_is_finalist(self):
        user = expert(BaseUserRole.FINALIST)
        self.assertTrue(is_finalist_user(user))

    def test_is_mentor(self):
        user = expert(BaseUserRole.MENTOR)
        self.assertTrue(is_mentor(user))

    def test_is_judge(self):
        user = expert(BaseUserRole.JUDGE)
        self.assertTrue(is_judge(user))

    def test_has_user_role_with_program(self):
        user = expert(BaseUserRole.FINALIST)
        self.assertFalse(is_finalist_user(user, ProgramFactory()))

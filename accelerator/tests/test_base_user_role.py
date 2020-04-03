# MIT License
# Copyright (c) 2019 MassChallenge, Inc.

from django.test import TestCase

from accelerator.tests.contexts import (
    JudgeFeedbackContext,
    UserRoleContext,
)
from accelerator_abstract.models.base_user_role import has_user_roles
from accelerator.models import (
    has_user_role_base,
    UserRole,
)


class TestBaseUserRole(TestCase):
    def test_has_user_role_base(self):
        context = JudgeFeedbackContext()
        judge = context.judge
        self.assertTrue(has_user_role_base(judge,
                                           UserRole.JUDGE,
                                           inactive_programs=True,
                                           active_or_ended_programs=True))

    def test_has_user_roles(self):
        context = UserRoleContext(user_role_name=UserRole.FINALIST)
        user = context.user
        self.assertTrue(has_user_roles(user,
                                       [UserRole.ALUM, UserRole.FINALIST]))

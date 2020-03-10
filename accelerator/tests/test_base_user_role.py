# MIT License
# Copyright (c) 2019 MassChallenge, Inc.

from django.test import TestCase

from accelerator.models import (
    has_user_role_base,
    UserRole,
)


class TestBaseUserRole(TestCase):
    def test_has_user_role_base(self):
        
        judge = context.judge
        self.assertTrue(has_user_role_base(judge,
                                           UserRole.JUDGE,
                                           inactive_programs=True,
                                           active_or_ended_programs=True))

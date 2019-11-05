# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import MemberFactory
from accelerator.tests.contexts import JudgeFeedbackContext
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
       
        


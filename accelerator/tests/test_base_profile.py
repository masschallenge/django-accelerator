# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories import MemberFactory


class TestBaseProfile(TestCase):
    def test_str_is_first_and_last_name(self):
        member = MemberFactory()
        display = member.baseprofile.__str__()
        self.assertNotIn(member.email, display)
        self.assertIn(member.first_name, display)
        self.assertIn(member.last_name, display)

    def test_str_defaults_to_email_if_first_or_last_names_are_missing(
            self):
        member = MemberFactory()
        member.first_name = ''
        member.save()
        display = member.baseprofile.__str__()
        self.assertIn(member.email, display)
        self.assertNotIn(member.last_name, display)

from __future__ import unicode_literals

from django.db import IntegrityError
from django.test import TestCase

from accelerator.models import BaseProfile
from accelerator.tests.factories import (
    CoreProfileModelFactory,
    MemberFactory,
)


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

    def test_manager_doesnt_to_create_memberprofile_for_unified_profiles(self):
        """
        Base profile manager should no longer attempt to create member
        profile objects for unified profile users. Attempting to create
        a member profile will raise IntegrityError
        """
        profile = CoreProfileModelFactory(expert_interest=True)
        try:
            BaseProfile.objects.get(email=profile.user.email)
        except IntegrityError:
            self.fail('Unexpectedly raised IntegrityError')

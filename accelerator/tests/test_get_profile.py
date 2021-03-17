# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db import IntegrityError
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from accelerator.models import (
    BaseProfile,
    ENTREPRENEUR_USER_TYPE,
    EXPERT_USER_TYPE,
    EntrepreneurProfile,
    ExpertProfile,
    MEMBER_USER_TYPE,
    MemberProfile,
)
from accelerator.models.profile_query_set import (
    INCORRECT_USER_TYPE_TEMPLATE,
    MISSING_BASE_PROFILE_TEMPLATE,
    MISSING_PROFILE_TEMPLATE,
)
from accelerator.tests.factories import (
    EntrepreneurFactory,
    ExpertFactory,
    MemberFactory,
)
from simpleuser.tests.factories import UserFactory

User = get_user_model()


class TestGetProfile(TestCase):
    def test_get_profile_returns_correct_profile_for_member(self):
        user = MemberFactory()
        profile = user.get_profile()
        self.assertIsInstance(profile, MemberProfile)

    def test_get_profile_returns_correct_profile_for_expert(self):
        user = ExpertFactory()
        profile = user.get_profile()
        self.assertIsInstance(profile, ExpertProfile)

    def test_get_profile_returns_correct_profile_for_entrepreneur(self):
        user = EntrepreneurFactory()
        profile = user.get_profile()
        self.assertIsInstance(profile, EntrepreneurProfile)

    def test_get_profile_works_by_primary_key(self):
        user = EntrepreneurFactory()
        profile = BaseProfile.objects.get(pk=user.pk)
        self.assertIsInstance(profile, EntrepreneurProfile)

    def test_get_profile_works_by_email_key(self):
        user = EntrepreneurFactory()
        profile = BaseProfile.objects.get(email=user.email)
        self.assertIsInstance(profile, EntrepreneurProfile)

    def test_get_profile_with_duplicate_emails_returns_integrity_error(self):
        user = EntrepreneurFactory()
        try:
            self.assertRaises(
                IntegrityError, EntrepreneurFactory(email=user.email))
        except IntegrityError:
            pass

    @patch("accelerator.models.profile_query_set.logger")
    def test_get_profile_handles_incorrect_user_type_member(self, mock_logger):
        member = MemberFactory()
        member.baseprofile.user_type = EXPERT_USER_TYPE
        member.baseprofile.save()
        profile = member.get_profile()
        self.assertIsInstance(profile, MemberProfile)
        member = User.objects.get(email=member.email)
        self.assertEqual(member.baseprofile.user_type, MEMBER_USER_TYPE)
        mock_logger.warning.assert_called_with(
            INCORRECT_USER_TYPE_TEMPLATE.format(EXPERT_USER_TYPE,
                                                MEMBER_USER_TYPE))

    @patch("accelerator.models.profile_query_set.logger")
    def test_get_profile_handles_incorrect_user_type_expert(self, mock_logger):
        expert = ExpertFactory()
        expert.baseprofile.user_type = ENTREPRENEUR_USER_TYPE
        expert.baseprofile.save()
        profile = expert.get_profile()
        self.assertIsInstance(profile, ExpertProfile)
        expert = User.objects.get(email=expert.email)
        self.assertEqual(expert.baseprofile.user_type, EXPERT_USER_TYPE)
        mock_logger.warning.assert_called_with(
            INCORRECT_USER_TYPE_TEMPLATE.format(ENTREPRENEUR_USER_TYPE,
                                                EXPERT_USER_TYPE))

    @patch("accelerator.models.profile_query_set.logger")
    def test_get_profile_handles_a_user_without_a_profile(self, mock_logger):
        entrepreneur = UserFactory()
        profile = BaseProfile.manager.filter(user=entrepreneur).first()
        assert profile is None
        profile = entrepreneur.get_profile()

        self.assertIsInstance(profile, MemberProfile)
        entrepreneur.refresh_from_db()
        self.assertEqual(entrepreneur.baseprofile.user_type, MEMBER_USER_TYPE)
        mock_logger.warning.assert_called_with(
            MISSING_PROFILE_TEMPLATE.format(MEMBER_USER_TYPE))
        mock_logger.warning.assert_any_call(
            MISSING_BASE_PROFILE_TEMPLATE.format(entrepreneur))

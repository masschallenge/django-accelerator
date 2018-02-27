# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories.interest_category_factory import (
    InterestCategoryFactory
)
from accelerator.tests.factories.member_profile_factory import (
    MemberProfileFactory
)
from accelerator.tests.factories.program_family_factory import (
    ProgramFamilyFactory
)
from accelerator.tests.factories.recommendation_tag_factory import (
    RecommendationTagFactory
)


class TestMemberProfile(TestCase):

    def test_create(self):
        profile = MemberProfileFactory()
        self.assertEqual(True, profile.user.is_active)

    def test_add_recommendation_tag(self):
        tag = RecommendationTagFactory()
        profile = MemberProfileFactory(recommendation_tags=[tag])
        self.assertTrue("tag_" in profile.recommendation_tags.all()[0].text)

    def test_add_program_family(self):
        family = ProgramFamilyFactory()
        profile = MemberProfileFactory(program_families=[family])
        self.assertTrue("Program Family" in
                        profile.program_families.all()[0].name)
        self.assertTrue(profile.current_program.program_family != family)

    def test_add_interest_categories(self):
        interest = InterestCategoryFactory()
        profile = MemberProfileFactory(current_program=interest.program,
                                       interest_categories=[interest])
        self.assertTrue("Interest Category" in
                        profile.interest_categories.all()[0].name)

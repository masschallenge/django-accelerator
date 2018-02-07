# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories.expert_profile_factory import ExpertProfileFactory
from accelerator.tests.factories.functional_expertise_factory import FunctionalExpertiseFactory
from accelerator.tests.factories.industry_factory import IndustryFactory
from accelerator.tests.factories.mentoring_specialties_factory import (
    MentoringSpecialtiesFactory,
)
from accelerator.models import (
    ExpertCategory,
    Industry,
)


class TestExpertProfile(TestCase):

    def test_create(self):
        profile = ExpertProfileFactory()
        self.assertEqual(True, profile.user.is_active)
        self.assertTrue("" != profile.bio)
        self.assertTrue(isinstance(profile.expert_category, ExpertCategory))
        self.assertTrue(isinstance(profile.primary_industry,
                                   Industry))

    def test_add_functional_expertise(self):
        profile = ExpertProfileFactory(
            functional_expertise=[FunctionalExpertiseFactory()])
        self.assertTrue("Functional Expertise" in
                        profile.functional_expertise.all()[0].name)

    def test_add_industries(self):
        profile = ExpertProfileFactory(
            additional_industries=[IndustryFactory()])
        self.assertTrue("Industry" in
                        profile.additional_industries.all()[0].name)

    def test_add_mentoring_specialty(self):
        profile = ExpertProfileFactory(
            mentoring_specialties=[MentoringSpecialtiesFactory()])
        self.assertTrue("Mentoring Specialties" in
                        profile.mentoring_specialties.all()[0].name)

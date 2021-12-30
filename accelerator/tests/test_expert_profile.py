from datetime import timedelta
from time import sleep

from django.test import TestCase

from accelerator.models import (
    ExpertCategory,
    Industry,
    UserRole,
)
from accelerator.models.expert_profile import SHORT_BIO_MAX_LENGTH
from accelerator.tests.contexts import UserRoleContext
from accelerator.tests.contexts.mentor_program_group_context import (
    MentorProgramGroupContext,
)
from accelerator.tests.contexts.mentor_user_context import MentorUserContext
from accelerator.tests.factories import (
    ExpertProfileFactory,
    FunctionalExpertiseFactory,
    IndustryFactory,
    MentoringSpecialtiesFactory,
    ProgramFactory,
    ProgramFamilyFactory,
)

from accelerator_abstract.models import (
    ACTIVE_PROGRAM_STATUS,
    BIO_MAX_LENGTH,
    ENDED_PROGRAM_STATUS,
    UPCOMING_PROGRAM_STATUS,
)

RAW_BIO = 'Lorem ipsum dolor sit amet ' * 500


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

    def test_mentor_profile_user_email(self):
        mentor = MentorUserContext().user
        mentor_profile = mentor.get_profile()
        self.assertTrue(mentor_profile.email() == mentor.email)

    def test_long_bio_does_not_exceed_max_length(self):
        expert_profile = ExpertProfileFactory(bio=RAW_BIO)
        self.assertTrue(len(expert_profile.long_bio) < BIO_MAX_LENGTH)

    def test_long_bio_is_trimmed(self):
        expert_profile = ExpertProfileFactory(bio=RAW_BIO)
        self.assertEqual(expert_profile.long_bio[-3:], '...')

    def test_short_bio_does_not_exceed_max_length(self):
        expert_profile = ExpertProfileFactory(bio=RAW_BIO)
        self.assertTrue(len(expert_profile.short_bio) < SHORT_BIO_MAX_LENGTH)

    def test_short_bio_is_trimmed(self):
        expert_profile = ExpertProfileFactory(bio=RAW_BIO)
        self.assertEqual(expert_profile.short_bio[-3:], '...')

    def test_mentor_profile_user_first_name(self):
        mentor = MentorUserContext().user
        mentor_profile = mentor.get_profile()
        self.assertTrue(mentor_profile.first_name() == mentor.first_name)

    def test_mentor_profile_user_last_name(self):
        mentor = MentorUserContext().user
        mentor_profile = mentor.get_profile()
        self.assertTrue(mentor_profile.last_name() == mentor.last_name)

    def test_mentor_profile_additional_industry_names(self):
        mentor_profile = ExpertProfileFactory(
            additional_industries=[IndustryFactory()])
        additional_industry_names = [
            industry.name for industry in (
                mentor_profile.additional_industries.all())]
        self.assertTrue(mentor_profile.additional_industry_names() == (
            additional_industry_names))

    def test_mentor_profile_mentoring_specialty_names(self):
        mentor_profile = ExpertProfileFactory(
            mentoring_specialties=[MentoringSpecialtiesFactory()])
        mentoring_specialties = [
            str(specialty) for specialty in (
                mentor_profile.mentoring_specialties.all())]
        self.assertTrue(mentor_profile.mentoring_specialty_names() == (
            mentoring_specialties))

    def test_mentor_profile_functional_expertise_names(self):
        mentor_profile = ExpertProfileFactory(
            functional_expertise=[FunctionalExpertiseFactory()])
        functional_expertise_names = [
            expertise.name for expertise in (
                mentor_profile.functional_expertise.all())]
        self.assertTrue(
            mentor_profile.functional_expertise_names() == (
                functional_expertise_names))

    def test_is_confirmed_mentor_returns_for_confirmed_mentors(self):
        context = MentorProgramGroupContext()
        confirmed = context.mentors[0]
        non_confirmed_mentor = context.mentors[1]
        non_confirmed_mentor.programrolegrant_set.all().delete()
        UserRoleContext(UserRole.MENTOR)
        self.assertTrue(confirmed.get_profile().is_confirmed_mentor())
        self.assertFalse(
            non_confirmed_mentor.get_profile().is_confirmed_mentor())

    def test_confirmed_mentor_programs(self):
        context = MentorProgramGroupContext()
        program = context.programs[0]
        confirmed = context.mentors[0]
        UserRoleContext(UserRole.MENTOR,
                        program=program)
        mentor_profile = confirmed.get_profile()
        confirmed_programs = mentor_profile.confirmed_mentor_programs()
        self.assertTrue(
            program.name in confirmed_programs)

    def test_latest_active_program_location_is_by_grant_create_time(self):
        context = MentorUserContext()
        confirmed_mentor = context.user
        program = context.program
        another_program = ProgramFactory(
            start_date=(program.start_date - timedelta(1)),
            end_date=(program.end_date - timedelta(1))
        )
        sleep(1)  # otherwise created_at fields are treated as equal
        later_prg_context = MentorUserContext(user=confirmed_mentor,
                                              program=another_program)
        mentor_profile = confirmed_mentor.get_profile()

        program_location = mentor_profile.latest_active_program_location()

        self.assertGreater(later_prg_context.program_role_grant.created_at,
                           context.program_role_grant.created_at)
        self.assertEqual(program_location,
                         another_program.program_family.name)

    def test_latest_active_program_location_for_unconfirmed_is_none(self):
        program_role = UserRoleContext(
            UserRole.DESIRED_MENTOR).program_role
        context = MentorUserContext(program_role=program_role)
        desired_mentor_profile = context.user.get_profile()

        program_location = (
            desired_mentor_profile.latest_active_program_location())

        self.assertIsNone(program_location)

    def test_latest_active_program_location_for_upcoming_program_is_none(self):
        program = ProgramFactory(program_status=UPCOMING_PROGRAM_STATUS)
        context = MentorUserContext(program=program)
        desired_mentor_profile = context.user.get_profile()

        program_location = (
            desired_mentor_profile.latest_active_program_location())

        self.assertIsNone(program_location)

    def test_latest_active_program_year_for_unconfirmed_is_none(self):
        program_role = UserRoleContext(
            UserRole.DESIRED_MENTOR).program_role
        context = MentorUserContext(program_role=program_role)
        desired_mentor_profile = context.user.get_profile()

        program_year = desired_mentor_profile.latest_active_program_year()

        self.assertIsNone(program_year)

    def test_latest_active_program_year_for_upcoming_program_is_none(self):
        program = ProgramFactory(program_status=UPCOMING_PROGRAM_STATUS)
        context = MentorUserContext(program=program)
        desired_mentor_profile = context.user.get_profile()

        program_year = desired_mentor_profile.latest_active_program_year()

        self.assertIsNone(program_year)

    def test_confirmed_mentor_program_families(self):
        confirmed_mentor = _user_grant_program(ACTIVE_PROGRAM_STATUS,
                                               "active_program_family")
        _user_grant_program(ENDED_PROGRAM_STATUS,
                            "ended_program_family",
                            confirmed_mentor)
        _user_grant_program(UPCOMING_PROGRAM_STATUS,
                            "upcoming_program_family",
                            confirmed_mentor)
        mentor_profile = confirmed_mentor.get_profile()
        program_families = mentor_profile.confirmed_mentor_program_families()
        self.assertEqual(['active_program_family', 'ended_program_family'],
                         program_families)

    def test_only_recent_program_program_families_are_returned(self):
        program_family = ProgramFamilyFactory(name="shared_program_family")
        confirmed_mentor = _user_grant_program(ENDED_PROGRAM_STATUS,
                                               program_family=program_family)
        mentor_profile = confirmed_mentor.get_profile()
        program_families = mentor_profile.confirmed_mentor_program_families()
        self.assertIn('shared_program_family', program_families)

        ProgramFactory(program_family=program_family)
        program_families = mentor_profile.confirmed_mentor_program_families()
        self.assertNotIn('shared_program_family', program_families)


def _user_grant_program(program_status, program_family_name=None,
                        user=None, program_family=None):
    program = ProgramFactory(
        program_status=program_status,
        program_family=program_family or ProgramFamilyFactory(
            name=program_family_name))
    context = MentorUserContext(program=program, user=user)
    return context.user

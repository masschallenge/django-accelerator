# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    ClearanceFactory,
    ExpertFactory,
    EntrepreneurFactory,
    EntrepreneurProfileFactory,
    InterestCategoryFactory,
    MemberFactory,
    ProgramFactory,
    ProgramRoleFactory,
    ProgramRoleGrantFactory,
    UserFactory,
    UserRoleFactory,
    ProgramFamilyFactory,
    PartnerTeamMemberFactory,
)
from accelerator_abstract.models import (
    BaseUserRole,
    ENDED_PROGRAM_STATUS,
)
from accelerator.tests.contexts import (
    StartupTeamMemberContext,
    UserRoleContext,
)
from accelerator_abstract.models.base_clearance import (
    CLEARANCE_LEVEL_STAFF,
)


def expert(role):
    user = ExpertFactory()
    profile = user.get_profile()
    profile.save()
    ur = UserRoleFactory(name=role)
    pr = ProgramRoleFactory.create(user_role=ur)
    ProgramRoleGrantFactory.create(person=user, program_role=pr)
    return user


class TestCoreProfile(TestCase):
    def test_full_name(self):
        user = ExpertFactory(first_name="", last_name="")
        self.assertTrue(user.get_profile().full_name() == str(user.email))

    def test_str(self):
        user = ExpertFactory()
        profile = user.get_profile()
        self.assertTrue(profile.full_name() in str(profile))

    def test_mentor_is_office_hour_holder(self):
        user = expert(BaseUserRole.MENTOR)
        self.assertTrue(user.get_profile().is_office_hour_holder())

    def test_partner_is_office_hour_holder(self):
        user = expert(BaseUserRole.PARTNER)
        self.assertTrue(user.get_profile().is_office_hour_holder())

    def test_partner_admin_is_office_hour_holder(self):
        user = expert(BaseUserRole.PARTNER_ADMIN)
        self.assertTrue(user.get_profile().is_office_hour_holder())

    def test_alumni_in_residence_is_office_hour_holder(self):
        user = expert(BaseUserRole.AIR)
        self.assertTrue(user.get_profile().is_office_hour_holder())

    def test_user_roles(self):
        user = ExpertFactory()
        user_role_names = [BaseUserRole.MENTOR,
                           BaseUserRole.STAFF,
                           BaseUserRole.AIR]
        for role_name in user_role_names:
            ur = UserRoleFactory(name=role_name)
            pr1 = ProgramRoleFactory.create(name=role_name + "1",
                                            user_role=ur)
            pr2 = ProgramRoleFactory.create(name=role_name + "2",
                                            user_role=ur)
            ProgramRoleGrantFactory.create(person=user,
                                           program_role=pr1)
            ProgramRoleGrantFactory.create(person=user,
                                           program_role=pr2)
        self.assertTrue(len(user.get_profile().user_roles()) ==
                        len(user_role_names))

    def test_active_alerts(self):
        member = MemberFactory()
        self.assertTrue(len(member.get_profile().get_active_alerts()) == 0)

    def test_is_judge_is_false_by_default(self):
        user = expert(BaseUserRole.FINALIST)
        self.assertFalse(user.get_profile().is_judge())

    def test_is_program_graduate_is_false_by_default(self):
        user = expert(BaseUserRole.FINALIST)
        self.assertFalse(user.get_profile().is_program_graduate())

    def test_first_startup_is_false_by_default(self):
        user = expert(BaseUserRole.FINALIST)
        self.assertFalse(user.get_profile().first_startup())

    def test_program_family_names(self):
        user = expert(BaseUserRole.FINALIST)
        profile = user.get_profile()
        family = ProgramFamilyFactory()
        profile.program_families.add(family)
        self.assertTrue(profile.program_family_names() == [family.name])

    def test_interest_category_names(self):
        user = expert(BaseUserRole.FINALIST)
        profile = user.get_profile()
        interest_category = InterestCategoryFactory()
        profile.interest_categories.add(interest_category)
        self.assertTrue(
            profile.interest_category_names() == [interest_category.name])

    def test_expert_is_alum_in_residence(self):
        user = expert(BaseUserRole.AIR)
        profile = user.get_profile()
        self.assertTrue(profile.is_alum_in_residence())

    def test_is_partner(self):
        user = expert(BaseUserRole.FINALIST)
        PartnerTeamMemberFactory(team_member=user)
        profile = user.get_profile()
        self.assertTrue(profile.is_partner())

    def test_is_partner_admin(self):
        user = expert(BaseUserRole.FINALIST)
        PartnerTeamMemberFactory(
            team_member=user, partner_administrator=True)
        profile = user.get_profile()
        self.assertTrue(profile.is_partner_admin())

    def test_is_mentor(self):
        user = expert(BaseUserRole.MENTOR)
        profile = user.get_profile()
        self.assertTrue(profile.is_mentor())

    def test_is_mentor_with_program_passed_in(self):
        user = expert(BaseUserRole.MENTOR)
        profile = user.get_profile()
        self.assertFalse(profile.is_mentor(ProgramFactory()))

    def test_role_based_landing_page(self):
        page = "/asante"
        context = StartupTeamMemberContext(
            primary_contact=False)
        ur = UserRoleFactory(name=BaseUserRole.FINALIST)
        pr = ProgramRoleFactory.create(
            user_role=ur,
            program=context.program,
            landing_page=page)
        ProgramRoleGrantFactory.create(person=context.user, program_role=pr)
        profile = context.user.get_profile()
        self.assertTrue(profile.role_based_landing_page() == page)

    def test_role_based_landing_page_excluding_roles(self):
        page = "/asante"
        context = StartupTeamMemberContext(
            primary_contact=False)
        ur = UserRoleFactory(name=BaseUserRole.FINALIST)
        pr = ProgramRoleFactory.create(
            user_role=ur,
            program=context.program,
            landing_page=page)
        ProgramRoleGrantFactory.create(person=context.user, program_role=pr)
        profile = context.user.get_profile()
        landing_page = profile.role_based_landing_page(exclude_role_names=[
            BaseUserRole.FINALIST
        ])
        default_page = profile.default_page
        self.assertTrue(landing_page == default_page)

    def test_entrepreneur_profile_has_confirmed_mentor_programs_prop(self):
        mentor = EntrepreneurFactory()
        attr = hasattr(mentor.get_profile(), "confirmed_mentor_programs")
        self.assertTrue(attr)

    def test_expert_profile_has_confirmed_mentor_programs_prop(self):
        expert = ExpertFactory()
        attr = hasattr(expert.get_profile(), "confirmed_mentor_programs")
        self.assertTrue(attr)

    def test_expert_profile_has_confirmed_mentor_program_families_all_prop(
            self):
        expert = ExpertFactory()
        attr = hasattr(expert.get_profile(),
                       "confirmed_memtor_program_families_all")
        self.assertTrue(attr)

    def test_user_is_a_previous_finalist_in_a_specified_program(self):
        user = EntrepreneurFactory()
        ended_program = ProgramFactory(program_status=ENDED_PROGRAM_STATUS)
        UserRoleContext(
            BaseUserRole.FINALIST,
            program=ended_program,
            user=user)
        self.assertTrue(user.get_profile().is_program_graduate(ended_program))

    def test_confirmed_mentor_programs(self):
        expert = ExpertFactory()
        context = UserRoleContext(
            BaseUserRole.MENTOR,
            user=expert)
        programs = expert.get_profile().confirmed_mentor_programs()
        self.assertTrue(len(programs), 1)
        self.assertIn(context.program.name, programs)

    def test_user_profile_confirmed_mentor_program_families_method(self):
        active_program = ProgramFactory()
        inactive_program = ProgramFactory(program_status=ENDED_PROGRAM_STATUS)
        user = EntrepreneurFactory()
        UserRoleContext(
            BaseUserRole.MENTOR,
            user=user,
            program=active_program)
        UserRoleContext(
            BaseUserRole.MENTOR,
            user=user,
            program=inactive_program)
        families = user.get_profile().confirmed_memtor_program_families_all()
        self.assertEqual(len(families), 2)
        self.assertTrue(active_program.program_family.name in families)
        self.assertTrue(inactive_program.program_family.name in families)

    def test_calc_landing_page_with_staff_user(self):
        user = UserFactory()
        ClearanceFactory(
            user=user,
            level=CLEARANCE_LEVEL_STAFF)
        landing_page = user.get_profile().calc_landing_page()
        self.assertEqual(landing_page, '/staff')

    def test_landing_page_if_profile_landing_page_is_set(self):
        test_landing_page = "/foobar"
        user_profile = EntrepreneurProfileFactory(
            landing_page=test_landing_page)
        landing_page = user_profile.check_landing_page()
        self.assertEqual(landing_page, test_landing_page)

    def test_landing_page_if_profile_landing_page_is_set_to_home(self):
        user_profile = EntrepreneurProfileFactory(landing_page="/")
        landing_page = user_profile.check_landing_page()
        self.assertEqual(landing_page, user_profile.default_page)

    def test_is_alum_in_residence(self):
        self.assertTrue(_user_is_alum_in_residence())

    def test_is_alum_in_residence_returns_true_if_in_program(self):
        air_program = ProgramFactory()
        self.assertTrue(_user_is_alum_in_residence(air_program))

    def test_is_alum_in_residence_returns_false_if_not_in_program(self):
        air_program = ProgramFactory()
        non_air_program = ProgramFactory()
        self.assertFalse(_user_is_alum_in_residence(
            air_program, non_air_program))


def _user_is_alum_in_residence(air_program=None, non_air_program=None):
    user = EntrepreneurFactory()
    context = UserRoleContext(
        BaseUserRole.AIR, user=user, program=air_program)
    user_profile = context.user.get_profile()
    program_of_interest = non_air_program or air_program
    if program_of_interest:
        return user_profile.is_alum_in_residence(program_of_interest)
    return user_profile.is_alum_in_residence()

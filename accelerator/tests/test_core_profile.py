# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    ExpertFactory,
    EntrepreneurFactory,
    InterestCategoryFactory,
    MemberFactory,
    ProgramFactory,
    ProgramRoleFactory,
    ProgramRoleGrantFactory,
    StartupFactory,
    UserRoleFactory,
    ProgramFamilyFactory,
    PartnerTeamMemberFactory
)
from accelerator_abstract.models import (
    BaseUserRole
)
from accelerator.tests.contexts import StartupTeamMemberContext


def expert(role):
    user = ExpertFactory()
    profile = user.get_profile()
    profile.gender = 'm'
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

    def test_is_alum_is_false_by_default(self):
        user = expert(BaseUserRole.FINALIST)
        self.assertFalse(user.get_profile().is_alum())

    def test_first_startup_is_false_by_default(self):
        user = expert(BaseUserRole.FINALIST)
        self.assertFalse(user.get_profile().first_startup())

    def test_gender_value_is_male(self):
        user = expert(BaseUserRole.FINALIST)
        profile = user.get_profile()
        self.assertTrue(profile.gender_value() == "Male")

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

    def test_is_alum_in_residence(self):
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

    def test_startup_based_landing_page(self):
        page = "/asante"
        startup = StartupFactory(landing_page=page)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup=startup)
        profile = context.user.get_profile()
        self.assertTrue(profile.startup_based_landing_page() == page)

    def test_startup_based_landing_page_returns_none_without_landpage(self):
        context = StartupTeamMemberContext(
            primary_contact=False)
        profile = context.user.get_profile()
        self.assertTrue(profile.startup_based_landing_page() is None)

    def test_check_landing_page(self):
        page = "/asante"
        startup = StartupFactory(landing_page=page)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup=startup)
        profile = context.user.get_profile()
        self.assertTrue(profile.check_landing_page() == page)

    def test_check_landing_page_with_landing_page_as_root(self):
        page = "/"
        startup = StartupFactory(landing_page=page)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup=startup)
        profile = context.user.get_profile()
        self.assertTrue(
            profile.check_landing_page() == profile.default_page)

    def test_calc_landing_page_with_landing_page(self):
        page = "/asante"
        startup = StartupFactory(landing_page=page)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup=startup)
        profile = context.user.get_profile()
        self.assertTrue(profile.calc_landing_page() == page)

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

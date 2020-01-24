# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.utils.six import StringIO

from datetime import datetime
from django.test import TestCase
from django.core.files.uploadedfile import InMemoryUploadedFile
from .factories.user_factory import UserFactory
from mock import MagicMock
from accelerator.tests.factories import (
    EntrepreneurFactory,
    ExpertFactory,
    IndustryFactory,
    ProgramFactory,
    StartupFactory,
    StartupStatusFactory,
    ProgramStartupStatusFactory,
    ProgramRoleGrantFactory,
    ProgramRoleFactory,
    UserRoleFactory,
    StartupTeamMemberFactory,
)
from accelerator.tests.contexts import (
    StartupTeamMemberContext
)
from simpleuser.models import User


class TestUser(TestCase):
    def test_str(self):
        user = UserFactory()
        assert user.email in str(user)

    def test_that_correct_entrepreneur_user_type_is_returned(self):
        user = EntrepreneurFactory()
        user = User.objects.get(pk=user.pk)
        self.assertEqual('entrepreneur', user.type())

    def test_that_correct_expert_user_type_is_returned(self):
        user = ExpertFactory()
        user = User.objects.get(pk=user.pk)
        self.assertEqual('expert', user.type())

    def test_startup_name_is_correct(self):
        context = StartupTeamMemberContext(primary_contact=False)
        startup = context.startup
        user = context.user
        self.assertEqual(startup.name, user.startup_name())

    def test_startup_industry_is_correct(self):
        context = StartupTeamMemberContext(primary_contact=False)
        startup = context.startup
        user = context.user
        self.assertEqual(startup.primary_industry,
                         user.startup_industry())

    def test_startup_top_level_industry_is_correct(self):
        industry = IndustryFactory(parent=IndustryFactory())
        startup = StartupFactory(primary_industry=industry)
        context = StartupTeamMemberContext(
            primary_contact=False, startup=startup)
        user = context.user
        self.assertEqual(industry.parent,
                         user.top_level_startup_industry())

    def test_location(self):
        program = ProgramFactory()
        user = User()
        user.program = MagicMock(return_value=program)
        self.assertEqual(program.program_family.name, user.location())

    def test_year(self):
        datetime_object = datetime.strptime('Jun 1 2005', '%b %d %Y')
        program = ProgramFactory(start_date=datetime_object)
        user = User()
        user.program = MagicMock(return_value=program)
        self.assertEqual(2005, user.year())

    def test_current_program(self):
        startup = StartupFactory()
        startup.current_program = MagicMock()
        user = User()
        user.startup = startup
        user.program()
        startup.current_program.assert_any_call()

    def test_expert_has_a_startup(self):
        expert = ExpertFactory()
        startup_name = expert.get_profile().company
        user = User.objects.get(pk=expert.pk)
        self.assertEqual(user.startup_name(), startup_name)

    def test_startup_team_member_has_a_startup(self):
        user = UserFactory()
        member = StartupTeamMemberFactory(user=user)
        self.assertEqual(user.startup_name(), member.startup.name)

    def test_user_without_a_startup(self):
        user = UserFactory()
        self.assertEqual(user.startup_name(), None)

    def test_expert_has_a_user_title(self):
        expert = ExpertFactory()
        title = expert.get_profile().title
        user = User.objects.get(pk=expert.pk)
        self.assertEqual(user.user_title(), title)

    def test_startup_team_member_has_a_title(self):
        user = UserFactory()
        member = StartupTeamMemberFactory(user=user)
        self.assertEqual(user.user_title(), member.title)

    def test_user_without_a_title(self):
        user = UserFactory()
        self.assertEqual(user.user_title(), "")

    def test_basic_getters_return_expected_results(self):
        user = ExpertFactory(
            profile__phone="111",
            profile__twitter_handle='tw0',
            profile__linked_in_url='http://www.linkedin.com/0',
            profile__facebook_url='http://www.facebook.com/0',
            profile__personal_website_url='http://example.com/0'
        )
        user = User.objects.get(pk=user.pk)
        self.assertEqual('111', user.user_phone())
        self.assertEqual('tw0', user.user_twitter_handle())
        self.assertEqual('http://www.linkedin.com/0',
                         user.user_linked_in_url())
        self.assertEqual('http://www.facebook.com/0',
                         user.user_facebook_url())
        self.assertEqual('http://example.com/0',
                         user.user_personal_website_url())

    def test_startup_status_names(self):
        status = ProgramStartupStatusFactory()
        context = StartupTeamMemberContext(primary_contact=False)
        StartupStatusFactory(startup=context.startup,
                             program_startup_status=status)
        status_names = context.user.startup_status_names()
        self.assertTrue(status.startup_status in status_names)

    def test_is_team_member_flag_on_user_with_startup(self):
        context = StartupTeamMemberContext(primary_contact=False)
        self.assertTrue(context.user.is_team_member())

    def test_is_team_member_flag_on_user_without_startup(self):
        user = UserFactory()
        self.assertFalse(user.is_team_member())

    def test_team_member_id_of_team_member(self):
        context = StartupTeamMemberContext(primary_contact=False)
        self.assertTrue(
            context.user.team_member_id() == context.member.id)

    def test_team_member_id_of_non_team_member(self):
        user = UserFactory()
        self.assertTrue(user.team_member_id() == '')

    def test_team_member_title(self):
        context = StartupTeamMemberContext(primary_contact=False)
        self.assertTrue(
            context.user.user_title() == context.member.title)

    def test_non_team_member_title(self):
        user = UserFactory()
        self.assertTrue(user.user_title() == '')

    def test_missing_profile_image_url_returns_empty(self):
        context = StartupTeamMemberContext(primary_contact=False)
        image_url = context.user.get_profile().image_url()
        self.assertTrue(context.user.image_url() == image_url)

    def test_s3_profile_image_url(self):
        context = StartupTeamMemberContext(primary_contact=False)
        user = context.user
        profile = user.get_profile()
        image = InMemoryUploadedFile(
            StringIO("test image data"),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len("test image data"),
            charset='utf-8',
        )
        profile.image = image
        profile.save()
        media_root = 'media'
        bucket_name = 'test-bucket'
        custom_domain_url = "{}.s3.amazonaws.com".format(bucket_name)
        with self.settings(**{
            'AWS_LOCATION': media_root,
            'AWS_ACCESS_KEY_ID': 'mock_access_key',
            'AWS_SECRET_ACCESS_KEY': 'mock_key',
            'AWS_STORAGE_BUCKET_NAME': bucket_name,
            'AWS_S3_CUSTOM_DOMAIN': custom_domain_url,
            'AWS_S3_OBJECT_PARAMETERS': {'CacheControl': 'max-age=86400'},
            'MEDIA_URL': 'https://{}/{}/'.format(
                custom_domain_url, media_root),
            'MEDIA_ROOT': media_root
        }):
            image_url = profile.image_url()
            self.assertTrue(
                image_url.startswith("https://{}/".format(custom_domain_url)))

    def test_finalist_user_roles(self):
        context = StartupTeamMemberContext(primary_contact=False)
        role_grant = ProgramRoleGrantFactory(
            person=context.user,
            program_role=ProgramRoleFactory(
                user_role=UserRoleFactory(name='Staff'))
        )
        finalist_roles = context.user.finalist_user_roles()
        self.assertTrue(role_grant.program_role.name in finalist_roles)

    def test_has_a_finalist_role(self):
        context = StartupTeamMemberContext(primary_contact=False)
        ProgramRoleGrantFactory(
            person=context.user,
            program_role=ProgramRoleFactory(
                user_role=UserRoleFactory(name='Staff'))
        )
        self.assertTrue(context.user.has_a_finalist_role())

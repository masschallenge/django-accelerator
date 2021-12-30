from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    OrganizationFactory,
    ProgramFactory,
    StartupFactory,
    StartupRoleFactory
)
from accelerator_abstract.models.base_startup_role import (
    BaseStartupRole
)
from accelerator_abstract.models.base_startup import (
    DISPLAY_STARTUP_STATUS
)
from accelerator.tests.contexts import (
    StartupTeamMemberContext
)


class TestStartup(TestCase):
    def test_startup(self):
        startup = StartupFactory()
        self.assertTrue(startup.organization.name in str(startup))

    def test_get_name(self):
        org = OrganizationFactory(name='foo')
        startup = StartupFactory(organization=org)
        self.assertEqual(org.name, startup.name)

    def test_set_name(self):
        org = OrganizationFactory(name='foo')
        startup = StartupFactory(organization=org)
        new_name = 'bar'
        startup.name = new_name
        startup.save()
        org.refresh_from_db()
        self.assertEqual(org.name, new_name)

    def test_get_website_url(self):
        org = OrganizationFactory(website_url='www.foo.com')
        startup = StartupFactory(organization=org)
        self.assertEqual(org.website_url, startup.website_url)

    def test_set_website_url(self):
        org = OrganizationFactory()
        startup = StartupFactory(organization=org)
        new_website_url = 'www.foo.com'
        startup.website_url = new_website_url
        startup.save()
        org.refresh_from_db()
        self.assertEqual(org.website_url, new_website_url)

    def test_get_twitter_handle(self):
        org = OrganizationFactory(twitter_handle='foo')
        startup = StartupFactory(organization=org)
        self.assertEqual(org.twitter_handle, startup.twitter_handle)

    def test_set_twitter_handle(self):
        org = OrganizationFactory()
        startup = StartupFactory(organization=org)
        new_twitter_handle = 'foo'
        startup.twitter_handle = new_twitter_handle
        startup.save()
        org.refresh_from_db()
        self.assertEqual(org.twitter_handle, new_twitter_handle)

    def test_get_public_inquiry_email(self):
        org = OrganizationFactory(public_inquiry_email='foo@bar.org')
        startup = StartupFactory(organization=org)
        self.assertEqual(org.public_inquiry_email,
                         startup.public_inquiry_email)

    def test_set_public_inquiry_email(self):
        org = OrganizationFactory()
        startup = StartupFactory(organization=org)
        new_public_inquiry_email = 'foo@bar.org'
        startup.public_inquiry_email = new_public_inquiry_email
        startup.save()
        org.refresh_from_db()
        self.assertEqual(org.public_inquiry_email, new_public_inquiry_email)

    def test_startup_with_no_org_does_not_cause_errors_on_read(self):
        startup = StartupFactory(organization=None)
        assert startup.organization is None
        try:
            startup.name
        except AttributeError:
            self.fail("Reading startup.name raised AttributeError")

    def test_startup_with_no_org_does_not_cause_errors_on_write(self):
        startup = StartupFactory(organization=None)
        assert startup.organization is None
        try:
            startup.name = "ZOMBOCOM"
        except AttributeError:
            self.fail("Setting startup.name raised AttributeError")

    def test_startup_repr_returns_empty_string_when_org_is_empty(self):
        startup = StartupFactory(organization=None)
        self.assertEqual(startup.__str__(), "")

    def test_is_finalist(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        self.assertTrue(context.startup.is_finalist())

    def test_is_finalist_with_program_passed_in(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        self.assertFalse(
            context.startup.is_finalist(ProgramFactory()))

    def test_generate_formatted_startup_status(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        program = context.program
        expected_status = DISPLAY_STARTUP_STATUS.format(
            status=BaseStartupRole.FINALIST,
            year=program.start_date.year,
            program_family_slug=program.program_family.url_slug.upper()
        )
        startup = context.startup
        finalist_statuses = startup._get_finalist_startup_statuses()
        self.assertEqual(
            startup._generate_formatted_startup_status(finalist_statuses[0]),
            expected_status
        )

    def test_get_finalist_startup_statuses(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        winner_role = StartupRoleFactory(name=BaseStartupRole.WINNER)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        context.create_startup_status(winner_role)
        startup = context.startup
        finalist_statuses = startup._get_finalist_startup_statuses()
        self.assertTrue(
            all([status in context.program_startup_statuses
                for status in finalist_statuses]))

    def test_finalist_startup_statuses_are_in_order_of_date_created(self):
        finalist_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        winner_role = StartupRoleFactory(name=BaseStartupRole.WINNER)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=finalist_role)
        context.create_startup_status(winner_role)
        finalist_statuses = context.startup.finalist_startup_statuses
        finalist_statuses.reverse()
        zipped_lists = zip(
            finalist_statuses, context.program_startup_statuses)
        startup = context.startup
        for status_string, status in zipped_lists:
            self.assertEqual(
                status_string,
                startup._generate_formatted_startup_status(status)
            )

    def test_latest_status_year_with_statuses(self):
        startup_role = StartupRoleFactory(name=BaseStartupRole.FINALIST)
        context = StartupTeamMemberContext(
            primary_contact=False,
            startup_role=startup_role)
        startup = context.startup
        startup_status = context.startup_statuses[0].program_startup_status
        program_year = startup_status.program.start_date.year
        self.assertEqual(startup.latest_status_year, program_year)

    def test_latest_status_year_without_startup_status(self):
        context = StartupTeamMemberContext(
            primary_contact=False)
        self.assertEqual(context.startup.latest_status_year, 0)

    def test_image_url_with_no_high_resolution_photo(self):
        context = StartupTeamMemberContext(
            primary_contact=False)
        self.assertEqual(context.startup.image_url, "")

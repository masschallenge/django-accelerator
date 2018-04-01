# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    OrganizationFactory,
    StartupFactory,
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

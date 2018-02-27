# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    OrganizationFactory,
    PartnerFactory,
)


class TestPartner(TestCase):

    def test_str(self):
        org = OrganizationFactory(name='foo')
        partner = PartnerFactory(organization=org)
        self.assertTrue(org.name in str(partner))

    def test_get_name(self):
        org = OrganizationFactory(name='foo')
        partner = PartnerFactory(organization=org)
        self.assertEqual(org.name, partner.name)

    def test_set_name(self):
        org = OrganizationFactory(name='foo')
        partner = PartnerFactory(organization=org)
        new_name = 'bar'
        partner.name = new_name
        partner.save()
        org.refresh_from_db()
        self.assertEqual(org.name, new_name)

    def test_get_website_url(self):
        org = OrganizationFactory(website_url='www.foo.com')
        partner = PartnerFactory(organization=org)
        self.assertEqual(org.website_url, partner.website_url)

    def test_set_website_url(self):
        org = OrganizationFactory()
        partner = PartnerFactory(organization=org)
        new_website_url = 'www.foo.com'
        partner.website_url = new_website_url
        partner.save()
        org.refresh_from_db()
        self.assertEqual(org.website_url, new_website_url)

    def test_get_twitter_handle(self):
        org = OrganizationFactory(twitter_handle='foo')
        partner = PartnerFactory(organization=org)
        self.assertEqual(org.twitter_handle, partner.twitter_handle)

    def test_set_twitter_handle(self):
        org = OrganizationFactory()
        partner = PartnerFactory(organization=org)
        new_twitter_handle = 'foo'
        partner.twitter_handle = new_twitter_handle
        partner.save()
        org.refresh_from_db()
        self.assertEqual(org.twitter_handle, new_twitter_handle)

    def test_get_public_inquiry_email(self):
        org = OrganizationFactory(public_inquiry_email='foo@bar.org')
        partner = PartnerFactory(organization=org)
        self.assertEqual(org.public_inquiry_email,
                         partner.public_inquiry_email)

    def test_set_public_inquiry_email(self):
        org = OrganizationFactory()
        partner = PartnerFactory(organization=org)
        new_public_inquiry_email = 'foo@bar.org'
        partner.public_inquiry_email = new_public_inquiry_email
        partner.save()
        org.refresh_from_db()
        self.assertEqual(org.public_inquiry_email, new_public_inquiry_email)

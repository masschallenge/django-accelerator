# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from django.test import TestCase

from accelerator.models import Organization
from accelerator.tests.factories import (
    OrganizationFactory,
)


class TestOrganization(TestCase):
    def test_organization(self):
        org = OrganizationFactory()
        self.assertNotEqual(org.url_slug, "")

    def test_organization_default_url_slug(self):
        org = OrganizationFactory(name=" ")
        self.assertEqual(org.url_slug, "organization")

    def test_str(self):
        org = OrganizationFactory()
        self.assertTrue(org.name in str(org))

    def test_organization_duplication(self):
        name = "My Organization"
        slug = slugify(name)
        organization1 = OrganizationFactory(name=name)
        organization2 = OrganizationFactory(name=name)
        assert organization1.url_slug != organization2.url_slug
        assert slug in organization1.url_slug
        assert slug in organization2.url_slug

    def test_slugify_org_with_no_name(self):
        org = OrganizationFactory(name="")
        slug = Organization.slug_from_instance(org)
        self.assertEqual(slug, "organization-1")

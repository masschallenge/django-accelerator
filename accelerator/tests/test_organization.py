# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from .factories.organization_factory import OrganizationFactory


class TestOrganization(TestCase):
    def test_organization(self):
        org = OrganizationFactory()
        self.assertNotEqual(org.url_slug, "")

    def test_organization_default(self):
        org = OrganizationFactory(name=" ")
        self.assertEqual(org.url_slug, "organization")

    def test_duplicate_organization_name(self):
        org1 = OrganizationFactory(name="Foo")
        org2 = OrganizationFactory(name="Foo")
        self.assertNotEqual(org1.url_slug, org2.url_slug)

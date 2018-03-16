# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import SiteFactory


class TestSite(TestCase):

    def test_str(self):
        site = SiteFactory()
        name = site.name
        url = site.site_url
        self.assertEqual(str(site), "{} at {}".format(name, url))

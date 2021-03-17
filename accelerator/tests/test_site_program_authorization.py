# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import SiteProgramAuthorizationFactory


class TestSiteProgramAuthorization(TestCase):

    def test_str(self):
        site_program_authorization = SiteProgramAuthorizationFactory(
            jobs=True,
            startup_list=False
        )
        assert site_program_authorization.site.name in str(
            site_program_authorization)
        assert site_program_authorization.program.name in str(
            site_program_authorization)
        assert "jobs" in str(site_program_authorization)
        assert "startup_list" not in str(site_program_authorization)

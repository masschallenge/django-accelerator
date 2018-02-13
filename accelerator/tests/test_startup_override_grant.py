# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    SiteProgramAuthorizationFactory,
    StartupOverrideGrantFactory,
)


class TestStartupOverrideGrant(TestCase):

    def test_str(self):
        startup_override_grant = StartupOverrideGrantFactory()
        assert startup_override_grant.program_override.name in str(
            startup_override_grant)
        assert startup_override_grant.program_override.program.name in str(
            startup_override_grant)
        assert startup_override_grant.startup.name in str(
            startup_override_grant)

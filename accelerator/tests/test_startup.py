# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from .factories.startup_factory import StartupFactory
from unittest import skip


# For some reason running StartupFactory() triggers an
# error that reports:
#
#   django.db.utils.OperationalError: no such table: auth_user
#
# AC-4806 is a bug ticket to fix this.

# @skip("StartupFactory generates an error.  See AC-4806")
class TestStartup(TestCase):
    def test_startup(self):
        startup = StartupFactory()
        self.assertTrue(startup.organization.name in str(startup))

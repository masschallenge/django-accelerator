# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from accelerator.tests.factories.startup_factory import StartupFactory


class TestStartup(TestCase):
    def test_startup(self):
        startup = StartupFactory()
        self.assertTrue(startup.organization.name in str(startup))

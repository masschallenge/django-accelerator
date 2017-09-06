# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from .factories.startup_factory import StartupFactory
from unittest import skip


class TestStartup(TestCase):
    def test_startup(self):
        startup = StartupFactory()
        self.assertTrue(startup.organization.name in str(startup))

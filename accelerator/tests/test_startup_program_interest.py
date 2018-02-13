# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import StartupProgramInterestFactory
from accelerator.models import StartupProgramInterest


class TestStartupProgramInterest(TestCase):

    def test_change_position(self):
        spi = StartupProgramInterestFactory()
        another_spi = StartupProgramInterestFactory(
            startup_cycle_interest=spi.startup_cycle_interest,
            startup=spi.startup
        )
        spis = StartupProgramInterest.objects.filter(startup=spi.startup)
        assert spis.first().id == spi.id

        spi.change_position(move="down")

        spis = StartupProgramInterest.objects.filter(startup=spi.startup)
        assert spis.first().id == another_spi.id

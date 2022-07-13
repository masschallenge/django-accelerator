from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import StartupProgramInterestFactory
from mc.models import StartupProgramInterest


class TestStartupProgramInterest(TestCase):
    def test_str(self):
        spi = StartupProgramInterestFactory()
        assert str(spi.program) in str(spi)
        assert str(spi.startup) in str(spi)
        assert str(spi.applying) in str(spi)

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

from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.startup_cycle_interest_factory import (
    StartupCycleInterestFactory
)

ProgramInterest = swapper.load_model('accelerator', 'ProgramInterest')


class ProgramInterestFactory(DjangoModelFactory):
    class Meta:
        model = ProgramInterest

    program = SubFactory(ProgramFactory)
    cycle_interest = SubFactory(StartupCycleInterestFactory)
    applying = False
    interest_level = ""

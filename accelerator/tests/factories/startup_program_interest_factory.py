from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.startup_cycle_interest_factory import (
    StartupCycleInterestFactory,
)
from accelerator.tests.factories.startup_factory import StartupFactory

StartupProgramInterest = swapper.load_model('accelerator',
                                            'StartupProgramInterest')


class StartupProgramInterestFactory(DjangoModelFactory):
    class Meta:
        model = StartupProgramInterest

    program = SubFactory(ProgramFactory)
    startup = SubFactory(StartupFactory)
    startup_cycle_interest = SubFactory(StartupCycleInterestFactory)
    applying = False
    order = Sequence(lambda x: x)
    interest_level = ""

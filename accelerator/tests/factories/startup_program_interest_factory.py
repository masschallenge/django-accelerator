# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.startup_cycle_interest_factory import (
    StartupCycleInterestFactory,
)
from accelerator.tests.factories.startup_factory import StartupFactory

StartupProgramInterest = swapper.load_model(AcceleratorConfig.name,
                                            'StartupProgramInterest')


class StartupProgramInterestFactory(DjangoModelFactory):
    class Meta:
        model = StartupProgramInterest

    program = SubFactory(ProgramFactory)
    startup = SubFactory(StartupFactory)
    startup_cycle_interest = SubFactory(StartupCycleInterestFactory)
    applying = False
    interest_level = ""

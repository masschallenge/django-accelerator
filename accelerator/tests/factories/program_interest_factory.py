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
    StartupCycleInterestFactory
)

ProgramInterest = swapper.load_model(AcceleratorConfig.name, 'ProgramInterest')


class ProgramInterestFactory(DjangoModelFactory):
    class Meta:
        model = ProgramInterest

    program = SubFactory(ProgramFactory)
    cycle_interest = SubFactory(StartupCycleInterestFactory)
    applying = False
    interest_level = ""

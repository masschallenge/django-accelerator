# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_cycle_factory import (
    ProgramCycleFactory
)
from accelerator.tests.factories.startup_factory import StartupFactory

StartupCycleInterest = swapper.load_model('accelerator',
                                          'StartupCycleInterest')


class StartupCycleInterestFactory(DjangoModelFactory):
    class Meta:
        model = StartupCycleInterest
        django_get_or_create = ('cycle', 'startup')

    cycle = SubFactory(ProgramCycleFactory)
    startup = SubFactory(StartupFactory)

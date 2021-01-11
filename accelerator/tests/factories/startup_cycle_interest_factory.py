# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.models import StartupCycleInterest
from accelerator.tests.factories.program_cycle_factory import (
    ProgramCycleFactory
)
from accelerator.tests.factories.startup_factory import StartupFactory


class StartupCycleInterestFactory(DjangoModelFactory):
    class Meta:
        model = StartupCycleInterest
        django_get_or_create = ('cycle', 'startup')

    cycle = SubFactory(ProgramCycleFactory)
    startup = SubFactory(StartupFactory)

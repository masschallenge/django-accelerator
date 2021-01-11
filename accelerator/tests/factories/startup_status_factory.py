# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_startup_status_factory import (
    ProgramStartupStatusFactory,
)
from accelerator.tests.factories.startup_factory import StartupFactory

from accelerator.models import StartupStatus


class StartupStatusFactory(DjangoModelFactory):
    class Meta:
        model = StartupStatus

    startup = SubFactory(StartupFactory)
    program_startup_status = SubFactory(ProgramStartupStatusFactory)

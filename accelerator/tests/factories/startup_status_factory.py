# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

StartupStatus = swapper.load_model(AcceleratorConfig.name, 'StartupStatus')

from accelerator.tests.factories.startup_factory import StartupFactory
from accelerator.tests.factories.program_startup_status_factory import (
    ProgramStartupStatusFactory,
)


class StartupStatusFactory(DjangoModelFactory):
    class Meta:
        model = StartupStatus

    startup = SubFactory(StartupFactory)
    program_startup_status = SubFactory(ProgramStartupStatusFactory)

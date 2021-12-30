from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_startup_status_factory import (
    ProgramStartupStatusFactory,
)
from accelerator.tests.factories.startup_factory import StartupFactory

StartupStatus = swapper.load_model('accelerator', 'StartupStatus')


class StartupStatusFactory(DjangoModelFactory):
    class Meta:
        model = StartupStatus

    startup = SubFactory(StartupFactory)
    program_startup_status = SubFactory(ProgramStartupStatusFactory)

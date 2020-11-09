# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from datetime import (
    datetime,
    timedelta,
)

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory
from pytz import utc

from accelerator.tests.factories.application_type_factory import (
    ApplicationTypeFactory
)
from accelerator.tests.factories.program_cycle_factory import (
    ProgramCycleFactory
)
from accelerator.tests.factories.startup_factory import StartupFactory
from accelerator_abstract.models.base_application import (
    INCOMPLETE_APP_STATUS,
)

Application = swapper.load_model('accelerator', 'Application')


class ApplicationFactory(DjangoModelFactory):
    class Meta:
        model = Application

    cycle = SubFactory(ProgramCycleFactory)
    startup = SubFactory(StartupFactory)
    application_type = SubFactory(ApplicationTypeFactory)
    application_status = INCOMPLETE_APP_STATUS
    submission_datetime = utc.localize(datetime.now() + timedelta(-2))

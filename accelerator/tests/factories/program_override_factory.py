# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from datetime import datetime

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from pytz import utc

from accelerator.tests.factories.program_cycle_factory import (
    ProgramCycleFactory
)
from accelerator.tests.factories.program_factory import ProgramFactory

ProgramOverride = swapper.load_model('accelerator', 'ProgramOverride')


class ProgramOverrideFactory(DjangoModelFactory):
    class Meta:
        model = ProgramOverride

    program = SubFactory(ProgramFactory)
    cycle = SubFactory(ProgramCycleFactory)
    name = Sequence(lambda n: "{0}".format(n))
    applications_open = True
    application_open_date = utc.localize(datetime(2015, 1, 1))
    application_early_deadline_date = utc.localize(datetime(2015, 1, 8))
    application_final_deadline_date = utc.localize(datetime(2015, 1, 15))
    early_application_fee = 50.00
    regular_application_fee = 100

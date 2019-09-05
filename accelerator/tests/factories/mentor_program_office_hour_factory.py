# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from datetime import (
    date,
    datetime,
    time,
    timedelta,
)
from pytz import utc
import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.models import MC_BOS_LOCATION
from accelerator.tests.factories import (
    EntrepreneurFactory,
    ExpertFactory,
)
from accelerator.tests.factories.program_factory import ProgramFactory

MentorProgramOfficeHour = swapper.load_model(AcceleratorConfig.name,
                                             'MentorProgramOfficeHour')


class MentorProgramOfficeHourFactory(DjangoModelFactory):
    class Meta:
        model = MentorProgramOfficeHour

    program = SubFactory(ProgramFactory)
    mentor = SubFactory(ExpertFactory)
    finalist = SubFactory(EntrepreneurFactory)
    start_date_time = utc.localize(datetime.combine(
        date.today() + timedelta(days=3),
        time(hour=10)))
    end_date_time = utc.localize(datetime.combine(
        date.today() + timedelta(days=3),
        time(hour=12)))
    old_location = MC_BOS_LOCATION
    description = Sequence(lambda n: "Description office hour {0}".format(n))
    notify_reservation = True
    topics = Sequence(lambda n: "Topics for test office hour {0}".format(n))

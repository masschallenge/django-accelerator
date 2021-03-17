# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from datetime import (
    date,
    datetime,
    time,
    timedelta,
)
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from pytz import utc

from accelerator.tests.factories import (
    EntrepreneurFactory,
    ExpertFactory,
)
from accelerator.tests.factories.location_factory import LocationFactory
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.startup_factory import StartupFactory

MentorProgramOfficeHour = swapper.load_model('accelerator',
                                             'MentorProgramOfficeHour')


class MentorProgramOfficeHourFactory(DjangoModelFactory):
    class Meta:
        model = MentorProgramOfficeHour

    program = SubFactory(ProgramFactory)
    mentor = SubFactory(ExpertFactory)
    finalist = SubFactory(EntrepreneurFactory)
    startup = SubFactory(StartupFactory)
    start_date_time = utc.localize(datetime.combine(
        date.today() + timedelta(days=3),
        time(hour=10)))
    end_date_time = utc.localize(datetime.combine(
        date.today() + timedelta(days=3),
        time(hour=12)))
    location = SubFactory(LocationFactory)
    description = Sequence(lambda n: "Description office hour {0}".format(n))
    notify_reservation = True
    topics = Sequence(lambda n: "Topics for test office hour {0}".format(n))
    meeting_info = Sequence(lambda n: "{0} zoom link".format(n))

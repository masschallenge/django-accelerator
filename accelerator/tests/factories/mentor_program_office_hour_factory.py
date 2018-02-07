from datetime import (
    date,
    timedelta,
)

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
    date = date.today() + timedelta(days=3)
    start_time = '10:00'
    end_time = '12:00'
    location = MC_BOS_LOCATION
    description = Sequence(lambda n: "Description office hour {0}".format(n))
    notify_reservation = True
    topics = Sequence(lambda n: "Topics for test office hour {0}".format(n))

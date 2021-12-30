from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.startup_factory import StartupFactory

StartupMentorTrackingRecord = swapper.load_model('accelerator',
                                                 'StartupMentorTrackingRecord')


class StartupMentorTrackingRecordFactory(DjangoModelFactory):
    class Meta:
        model = StartupMentorTrackingRecord

    startup = SubFactory(StartupFactory)
    program = SubFactory(ProgramFactory)
    notes = Sequence(lambda n: "List of Goals {0}".format(n))

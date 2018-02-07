import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.startup_factory import StartupFactory

StartupMentorTrackingRecord = swapper.load_model(AcceleratorConfig.name,
                                                 'StartupMentorTrackingRecord')


class StartupMentorTrackingRecordFactory(DjangoModelFactory):
    class Meta:
        model = StartupMentorTrackingRecord

    startup = SubFactory(StartupFactory)
    program = SubFactory(ProgramFactory)
    notes = Sequence(lambda n: "List of Goals {0}".format(n))

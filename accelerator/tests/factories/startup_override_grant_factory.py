import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

StartupOverrideGrant = swapper.load_model(AcceleratorConfig.name,
                                          'StartupOverrideGrant')

from accelerator.tests.factories import (
    ProgramOverrideFactory,
    StartupFactory,
)


class StartupOverrideGrantFactory(DjangoModelFactory):
    class Meta:
        model = StartupOverrideGrant

    startup = SubFactory(StartupFactory)
    program_override = SubFactory(ProgramOverrideFactory)

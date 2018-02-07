import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

StartupAttribute = swapper.load_model(AcceleratorConfig.name,
                                      'StartupAttribute')

from accelerator.tests.factories.program_startup_attribute_factory import (
    ProgramStartupAttributeFactory,
)
from accelerator.tests.factories.startup_factory import StartupFactory


class StartupAttributeFactory(DjangoModelFactory):
    class Meta:
        model = StartupAttribute

    startup = SubFactory(StartupFactory)
    attribute = SubFactory(ProgramStartupAttributeFactory)
    attribute_value = Sequence(lambda n: "Attribute Value {0}".format(n))

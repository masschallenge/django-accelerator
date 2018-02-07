import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

StartupRole = swapper.load_model(AcceleratorConfig.name, 'StartupRole')


class StartupRoleFactory(DjangoModelFactory):
    class Meta:
        model = StartupRole

    name = Sequence(lambda x: "StartupRole %d" % x)

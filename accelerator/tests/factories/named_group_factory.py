import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

NamedGroup = swapper.load_model(AcceleratorConfig.name, 'NamedGroup')


class NamedGroupFactory(DjangoModelFactory):
    name = Sequence(lambda n: "Named Group {0}".format(n))

    class Meta:
        model = NamedGroup

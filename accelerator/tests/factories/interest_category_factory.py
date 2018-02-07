import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

InterestCategory = swapper.load_model(AcceleratorConfig.name,
                                      'InterestCategory')

from accelerator.tests.factories.program_factory import ProgramFactory


class InterestCategoryFactory(DjangoModelFactory):
    class Meta:
        model = InterestCategory

    name = Sequence(lambda n: "Interest Category {0}".format(n))
    program = SubFactory(ProgramFactory)

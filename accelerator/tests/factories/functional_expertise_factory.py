import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    post_generation,
)

from accelerator.apps import AcceleratorConfig

FunctionalExpertise = swapper.load_model(AcceleratorConfig.name,
                                         'FunctionalExpertise')


class FunctionalExpertiseFactory(DjangoModelFactory):
    class Meta:
        model = FunctionalExpertise

    name = Sequence(lambda n: "Functional Expertise {0}".format(n))

    @post_generation
    def parent(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.parent = extracted

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    post_generation,
)

from accelerator.apps import AcceleratorConfig

StartupLabel = swapper.load_model(AcceleratorConfig.name, 'StartupLabel')


class StartupLabelFactory(DjangoModelFactory):
    label = Sequence(lambda n: "Label {0}".format(n))

    class Meta:
        model = StartupLabel

    @post_generation
    def startups(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.startups.add(tag)

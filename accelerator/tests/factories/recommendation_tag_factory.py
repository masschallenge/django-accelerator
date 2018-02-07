import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

RecommendationTag = swapper.load_model(AcceleratorConfig.name,
                                       'RecommendationTag')


class RecommendationTagFactory(DjangoModelFactory):
    class Meta:
        model = RecommendationTag

    text = Sequence(lambda n: "tag_{0}".format(n))

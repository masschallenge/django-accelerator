from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import InnovationStage


class InnovationStageFactory(DjangoModelFactory):
    class Meta:
        model = InnovationStage
        django_get_or_create = ['name']

    name = Sequence(lambda n: "Innovation Stage {}".format(n))
    description = Sequence(
        lambda n: "Description of Innovation Stage {}".format(n))
    display_priority = Sequence(lambda n: n)
    image = None

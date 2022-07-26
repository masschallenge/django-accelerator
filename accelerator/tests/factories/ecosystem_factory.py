from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import Ecosystem


class EcosystemFactory(DjangoModelFactory):
    class Meta:
        model = Ecosystem
        django_get_or_create = ['name']

    name = Sequence(lambda n: "Ecosystem {}".format(n))
    display_priority = Sequence(lambda n: n)

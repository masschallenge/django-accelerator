from factory import (
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.startup_factory import StartupFactory
from accelerator.models import BusinessProposition


class BusinessPropositionFactory(DjangoModelFactory):
    class Meta:
        model = BusinessProposition

    startup = SubFactory(StartupFactory)

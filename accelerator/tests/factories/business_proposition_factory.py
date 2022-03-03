from __future__ import unicode_literals

import swapper
from factory import (
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.startup_factory import StartupFactory

BusinessProposition = swapper.load_model('accelerator', 'BusinessProposition')


class BusinessPropositionFactory(DjangoModelFactory):
    class Meta:
        model = BusinessProposition

    startup = SubFactory(StartupFactory)

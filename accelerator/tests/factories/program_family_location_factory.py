from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories import (
    ProgramFamilyFactory,
)
from accelerator.tests.factories.location_factory import LocationFactory

ProgramFamilyLocation = swapper.load_model('accelerator',
                                           'ProgramFamilyLocation')


class ProgramFamilyLocationFactory(DjangoModelFactory):
    class Meta:
        model = ProgramFamilyLocation

    program_family = SubFactory(ProgramFamilyFactory)
    location = SubFactory(LocationFactory)
    primary = False

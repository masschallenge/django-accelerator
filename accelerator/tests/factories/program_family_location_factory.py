from __future__ import unicode_literals

from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.models import ProgramFamilyLocation
from accelerator.tests.factories import (
    ProgramFamilyFactory,
)
from accelerator.tests.factories.location_factory import LocationFactory


class ProgramFamilyLocationFactory(DjangoModelFactory):
    class Meta:
        model = ProgramFamilyLocation

    program_family = SubFactory(ProgramFamilyFactory)
    location = SubFactory(LocationFactory)
    primary = False

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories import (
    ProgramFamilyFactory,
)
from accelerator.tests.factories.location_factory import LocationFactory

ProgramFamilyLocation = swapper.load_model(AcceleratorConfig.name,
                                           'ProgramFamilyLocation')


class ProgramFamilyLocationFactory(DjangoModelFactory):
    class Meta:
        model = ProgramFamilyLocation

    program_family = SubFactory(ProgramFamilyFactory)
    location = SubFactory(LocationFactory)
    primary = False

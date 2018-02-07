# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.program_family_factory import (
    ProgramFamilyFactory
)
from accelerator.tests.factories.user_factory import UserFactory

Clearance = swapper.load_model(AcceleratorConfig.name, 'Clearance')

from accelerator.models import CLEARANCE_LEVEL_POM


class ClearanceFactory(DjangoModelFactory):
    class Meta:
        model = Clearance

    user = SubFactory(UserFactory)
    program_family = SubFactory(ProgramFamilyFactory)
    level = CLEARANCE_LEVEL_POM

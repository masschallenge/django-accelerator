# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig
from accelerator.models import CLEARANCE_LEVEL_POM
from accelerator.tests.factories.program_family_factory import (
    ProgramFamilyFactory
)
from simpleuser.tests.factories.user_factory import UserFactory

Clearance = swapper.load_model(AcceleratorConfig.name, 'Clearance')


class ClearanceFactory(DjangoModelFactory):
    class Meta:
        model = Clearance

    user = SubFactory(UserFactory)
    program_family = SubFactory(ProgramFamilyFactory)
    level = CLEARANCE_LEVEL_POM

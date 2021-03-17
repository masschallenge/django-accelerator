# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories import (
    ProgramOverrideFactory,
    StartupFactory,
)

StartupOverrideGrant = swapper.load_model('accelerator',
                                          'StartupOverrideGrant')


class StartupOverrideGrantFactory(DjangoModelFactory):
    class Meta:
        model = StartupOverrideGrant

    startup = SubFactory(StartupFactory)
    program_override = SubFactory(ProgramOverrideFactory)

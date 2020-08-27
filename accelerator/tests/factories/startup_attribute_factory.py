# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory


from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.program_startup_attribute_factory import (
    ProgramStartupAttributeFactory,
)
from accelerator.tests.factories.startup_factory import StartupFactory

StartupAttribute = swapper.load_model(AcceleratorConfig.name,
                                      'StartupAttribute')


class StartupAttributeFactory(DjangoModelFactory):
    class Meta:
        model = StartupAttribute

    startup = SubFactory(StartupFactory)
    attribute = SubFactory(ProgramStartupAttributeFactory)
    attribute_value = Sequence(lambda n: "Attribute Value {0}".format(n))

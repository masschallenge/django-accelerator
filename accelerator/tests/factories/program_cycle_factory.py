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
from accelerator.tests.factories.application_type_factory import (
    ApplicationTypeFactory
)
from accelerator.tests.utils import months_from_now

ProgramCycle = swapper.load_model(AcceleratorConfig.name, 'ProgramCycle')


class ProgramCycleFactory(DjangoModelFactory):
    class Meta:
        model = ProgramCycle

    name = Sequence(lambda n: "Program Cycle {0}".format(n))
    short_name = Sequence(lambda n: "C{0}".format(n))
    applications_open = False
    application_open_date = months_from_now(-5)
    application_early_deadline_date = months_from_now(-4)
    application_final_deadline_date = months_from_now(-3)
    advertised_final_deadline = months_from_now(-3)
    accepting_references = False
    default_application_type = SubFactory(ApplicationTypeFactory)
    default_overview_application_type = SubFactory(
        ApplicationTypeFactory)
    hidden = False

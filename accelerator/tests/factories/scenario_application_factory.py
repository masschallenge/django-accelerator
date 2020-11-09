# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.application_factory import ApplicationFactory
from accelerator.tests.factories.scenario_factory import ScenarioFactory

ScenarioApplication = swapper.load_model('accelerator',
                                         'ScenarioApplication')


class ScenarioApplicationFactory(DjangoModelFactory):
    class Meta:
        model = ScenarioApplication

    application = SubFactory(ApplicationFactory)
    scenario = SubFactory(ScenarioFactory)

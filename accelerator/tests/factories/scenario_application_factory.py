# -*- coding: utf-8 -*-

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

ScenarioApplication = swapper.load_model(AcceleratorConfig.name,
                                         'ScenarioApplication')

from accelerator.tests.factories.application_factory import ApplicationFactory
from accelerator.tests.factories.scenario_factory import ScenarioFactory


class ScenarioApplicationFactory(DjangoModelFactory):
    class Meta:
        model = ScenarioApplication

    application = SubFactory(ApplicationFactory)
    scenario = SubFactory(ScenarioFactory)

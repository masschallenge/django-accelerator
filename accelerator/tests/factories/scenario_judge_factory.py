# -*- coding: utf-8 -*-

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

ScenarioJudge = swapper.load_model(AcceleratorConfig.name, 'ScenarioJudge')

from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.scenario_factory import ScenarioFactory


class ScenarioJudgeFactory(DjangoModelFactory):
    class Meta:
        model = ScenarioJudge

    # Note: is_judge will not be true after this.
    # To get a real just you need to use a UserRoleContext.
    judge = SubFactory(ExpertFactory)
    scenario = SubFactory(ScenarioFactory)

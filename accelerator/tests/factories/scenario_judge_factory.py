# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.scenario_factory import ScenarioFactory

ScenarioJudge = swapper.load_model(AcceleratorConfig.name, 'ScenarioJudge')


class ScenarioJudgeFactory(DjangoModelFactory):
    class Meta:
        model = ScenarioJudge

    # Note: is_judge will not be true after this.
    # To get a real just you need to use a UserRoleContext.
    judge = SubFactory(ExpertFactory)
    scenario = SubFactory(ScenarioFactory)

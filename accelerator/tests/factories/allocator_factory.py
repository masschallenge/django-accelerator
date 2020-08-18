# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import SubFactory

from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig

from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory,
)
from accelerator.tests.factories.scenario_factory import ScenarioFactory


Allocator = swapper.load_model(AcceleratorConfig.name, 'Allocator')


class AllocatorFactory(DjangoModelFactory):
    class Meta:
        model = Allocator

    judging_round = SubFactory(JudgingRoundFactory)
    scenario = SubFactory(ScenarioFactory)

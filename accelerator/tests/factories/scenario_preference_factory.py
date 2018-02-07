# -*- coding: utf-8 -*-

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.models import (
    JUDGE_ENTITY,
    JUDGE_IS_FEMALE,
    MIN_PREFERENCE,
)

ScenarioPreference = swapper.load_model(AcceleratorConfig.name,
                                        'ScenarioPreference')

from accelerator.tests.factories.scenario_factory import ScenarioFactory


class ScenarioPreferenceFactory(DjangoModelFactory):
    class Meta:
        model = ScenarioPreference

    scenario = SubFactory(ScenarioFactory)
    priority = Sequence(lambda n: str(n))
    constraint_type = MIN_PREFERENCE
    entity_type = JUDGE_ENTITY
    entity_set = JUDGE_IS_FEMALE
    amount = 1

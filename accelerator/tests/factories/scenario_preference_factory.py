# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.models import (
    JUDGE_ENTITY,
    JUDGE_IS_FEMALE,
    MIN_PREFERENCE,
)
from accelerator.tests.factories.scenario_factory import ScenarioFactory

from accelerator.models import ScenarioPreference


class ScenarioPreferenceFactory(DjangoModelFactory):
    class Meta:
        model = ScenarioPreference

    scenario = SubFactory(ScenarioFactory)
    priority = Sequence(lambda n: str(n))
    constraint_type = MIN_PREFERENCE
    entity_type = JUDGE_ENTITY
    entity_set = JUDGE_IS_FEMALE
    amount = 1

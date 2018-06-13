# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)
Criterion = swapper.load_model(AcceleratorConfig.name, 'Criterion')


class CriterionFactory(DjangoModelFactory):
    class Meta:
        model = Criterion

    type = Sequence(lambda n: "Criterion type {0}".format(n))
    name = Sequence(lambda n: "Criterion {0}".format(n))
    count = Criterion.DEFAULT_COUNT
    weight = Criterion.DEFAULT_WEIGHT
    judging_round = SubFactory(JudgingRoundFactory)

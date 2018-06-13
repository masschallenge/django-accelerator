# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    #Sequence,
    SubFactory,
)
from pytz import utc

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.criterion_factory import (
    CriterionFactory
)
CriterionOptionSpec = swapper.load_model(AcceleratorConfig.name,
                                         'CriterionOptionSpec')


class CriterionOptionSpecFactory(DjangoModelFactory):
    class Meta:
        model = CriterionOptionSpec

    name = Sequence(lambda n: "CriterionOptionSpec {0}".format(n))
    count = CriterionOptionSpec.DEFAULT_COUNT
    weight = CriterionCriterionOptionSpec.DEFAULT_WEIGHT
    judging_round = SubFactory(CriterionFactory)

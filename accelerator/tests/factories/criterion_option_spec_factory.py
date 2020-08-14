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
from accelerator.tests.factories.criterion_factory import (
    CriterionFactory
)
CriterionOptionSpec = swapper.load_model(AcceleratorConfig.name,
                                         'CriterionOptionSpec')


class CriterionOptionSpecFactory(DjangoModelFactory):
    class Meta:
        model = CriterionOptionSpec

    option = Sequence(lambda n: "CriterionOptionSpec {0}".format(n))
    count = CriterionOptionSpec.DEFAULT_COUNT
    weight = CriterionOptionSpec.DEFAULT_WEIGHT
    criterion = SubFactory(CriterionFactory)

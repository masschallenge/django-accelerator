from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory
from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)
Criterion = swapper.load_model('accelerator', 'Criterion')


class CriterionFactory(DjangoModelFactory):
    class Meta:
        model = Criterion

    type = Sequence(lambda n: "Criterion type {0}".format(n))
    name = Sequence(lambda n: "Criterion {0}".format(n))
    judging_round = SubFactory(JudgingRoundFactory)

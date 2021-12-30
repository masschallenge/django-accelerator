from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.criterion_factory import (
    CriterionFactory
)
CriterionOptionSpec = swapper.load_model('accelerator', 'CriterionOptionSpec')


class CriterionOptionSpecFactory(DjangoModelFactory):
    class Meta:
        model = CriterionOptionSpec

    option = Sequence(lambda n: "CriterionOptionSpec {0}".format(n))
    count = CriterionOptionSpec.DEFAULT_COUNT
    weight = CriterionOptionSpec.DEFAULT_WEIGHT
    criterion = SubFactory(CriterionFactory)

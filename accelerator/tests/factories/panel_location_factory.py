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

PanelLocation = swapper.load_model('accelerator', 'PanelLocation')


class PanelLocationFactory(DjangoModelFactory):
    class Meta:
        model = PanelLocation

    location = Sequence(lambda n: "Location {0}".format(n))
    description = Sequence(lambda n: "Panel Location {0}".format(n))
    judging_round = SubFactory(JudgingRoundFactory)

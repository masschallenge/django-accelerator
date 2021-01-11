# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)

from accelerator.models import PanelLocation


class PanelLocationFactory(DjangoModelFactory):
    class Meta:
        model = PanelLocation

    location = Sequence(lambda n: "Location {0}".format(n))
    description = Sequence(lambda n: "Panel Location {0}".format(n))
    judging_round = SubFactory(JudgingRoundFactory)

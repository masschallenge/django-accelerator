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

PanelLocation = swapper.load_model(AcceleratorConfig.name, 'PanelLocation')

from accelerator.tests.factories.judging_round_factory import JudgingRoundFactory


class PanelLocationFactory(DjangoModelFactory):
    class Meta:
        model = PanelLocation

    location = Sequence(lambda n: "Location {0}".format(n))
    description = Sequence(lambda n: "Panel Location {0}".format(n))
    judging_round = SubFactory(JudgingRoundFactory)

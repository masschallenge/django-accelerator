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

PanelType = swapper.load_model(AcceleratorConfig.name, 'PanelType')


class PanelTypeFactory(DjangoModelFactory):
    class Meta:
        model = PanelType

    panel_type = Sequence(lambda n: "Panel Type {0}".format(n))
    description = Sequence(lambda n: "Panel Type Description {0}".format(n))
    judging_round = SubFactory(JudgingRoundFactory)

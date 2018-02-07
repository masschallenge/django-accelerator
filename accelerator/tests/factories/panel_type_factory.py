# -*- coding: utf-8 -*-

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

PanelType = swapper.load_model(AcceleratorConfig.name, 'PanelType')

from accelerator.tests.factories.judging_round_factory import JudgingRoundFactory


class PanelTypeFactory(DjangoModelFactory):
    class Meta:
        model = PanelType

    panel_type = Sequence(lambda n: "Panel Type {0}".format(n))
    description = Sequence(lambda n: "Panel Type Description {0}".format(n))
    judging_round = SubFactory(JudgingRoundFactory)

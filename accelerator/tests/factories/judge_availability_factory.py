# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.judge_round_commitment_factory import (
    JudgeRoundCommitmentFactory,
)
from accelerator.tests.factories.panel_location_factory import PanelLocationFactory
from accelerator.tests.factories.panel_time_factory import PanelTimeFactory
from accelerator.tests.factories.panel_type_factory import PanelTypeFactory

JudgeAvailability = swapper.load_model(AcceleratorConfig.name,
                                       'JudgeAvailability')


class JudgeAvailabilityFactory(DjangoModelFactory):
    class Meta:
        model = JudgeAvailability

    commitment = SubFactory(JudgeRoundCommitmentFactory)
    panel_location = SubFactory(PanelLocationFactory)
    panel_time = SubFactory(PanelTimeFactory)
    panel_type = SubFactory(PanelTypeFactory)
    availability_type = "Available"

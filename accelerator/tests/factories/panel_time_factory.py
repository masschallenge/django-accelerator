# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from datetime import timedelta

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)
from accelerator.tests.utils import months_from_now

PanelTime = swapper.load_model(AcceleratorConfig.name, 'PanelTime')


class PanelTimeFactory(DjangoModelFactory):
    class Meta:
        model = PanelTime

    start_date_time = months_from_now(1)
    end_date_time = months_from_now(1) + timedelta(hours=4)
    day = start_date_time.strftime("%A %-m/%-d")
    time = start_date_time.strftime("%I:%M%p")
    judging_round = SubFactory(JudgingRoundFactory)

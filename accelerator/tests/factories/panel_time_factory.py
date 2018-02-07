# -*- coding: utf-8 -*-

from datetime import timedelta

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

PanelTime = swapper.load_model(AcceleratorConfig.name, 'PanelTime')

from accelerator.tests.utils import months_from_now
from accelerator.tests.factories.judging_round_factory import JudgingRoundFactory


class PanelTimeFactory(DjangoModelFactory):
    class Meta:
        model = PanelTime

    start_date_time = months_from_now(1)
    end_date_time = months_from_now(1) + timedelta(hours=4)
    day = start_date_time.strftime("%A %-m/%-d")
    time = start_date_time.strftime("%I:%M%p")
    judging_round = SubFactory(JudgingRoundFactory)

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
from accelerator.models import PREVIEW_PANEL_STATUS

Panel = swapper.load_model(AcceleratorConfig.name, 'Panel')

from accelerator.tests.factories.panel_location_factory import PanelLocationFactory
from accelerator.tests.factories.panel_time_factory import PanelTimeFactory
from accelerator.tests.factories.panel_type_factory import PanelTypeFactory


class PanelFactory(DjangoModelFactory):
    class Meta:
        model = Panel

    panel_time = SubFactory(PanelTimeFactory)
    panel_type = SubFactory(PanelTypeFactory)
    description = Sequence(lambda n: "Panel Description {0}".format(n))
    location = SubFactory(PanelLocationFactory)
    status = PREVIEW_PANEL_STATUS

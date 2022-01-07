from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.models import PREVIEW_PANEL_STATUS
from accelerator.tests.factories.panel_location_factory import (
    PanelLocationFactory
)
from accelerator.tests.factories.panel_time_factory import PanelTimeFactory
from accelerator.tests.factories.panel_type_factory import PanelTypeFactory

Panel = swapper.load_model('accelerator', 'Panel')


class PanelFactory(DjangoModelFactory):
    class Meta:
        model = Panel

    panel_time = SubFactory(PanelTimeFactory)
    panel_type = SubFactory(PanelTypeFactory)
    description = Sequence(lambda n: "Panel Description {0}".format(n))
    location = SubFactory(PanelLocationFactory)
    status = PREVIEW_PANEL_STATUS

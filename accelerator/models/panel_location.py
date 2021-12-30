from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_panel_location import BasePanelLocation


class PanelLocation(BasePanelLocation):
    class Meta(BasePanelLocation.Meta):
        swappable = swapper.swappable_setting(
            BasePanelLocation.Meta.app_label, "PanelLocation")

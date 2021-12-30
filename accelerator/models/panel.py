from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_panel import BasePanel


class Panel(BasePanel):
    class Meta(BasePanel.Meta):
        swappable = swapper.swappable_setting(BasePanel.Meta.app_label,
                                              "Panel")

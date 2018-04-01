# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_panel_time import BasePanelTime


class PanelTime(BasePanelTime):
    class Meta(BasePanelTime.Meta):
        swappable = swapper.swappable_setting(
            BasePanelTime.Meta.app_label, "PanelTime")

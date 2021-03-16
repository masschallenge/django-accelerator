# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_panel_type import BasePanelType


class PanelType(BasePanelType):
    class Meta(BasePanelType.Meta):
        swappable = swapper.swappable_setting(
            BasePanelType.Meta.app_label, "PanelType")

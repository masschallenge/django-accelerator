# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_panel_type import BasePanelType


class PanelType(BasePanelType):
    class Meta(BasePanelType.Meta):
        swappable = False

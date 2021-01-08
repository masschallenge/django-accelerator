# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_panel_location import BasePanelLocation


class PanelLocation(BasePanelLocation):
    class Meta(BasePanelLocation.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper
from accelerator_abstract.models.base_application_panel_assignment import (
    BaseApplicationPanelAssignment
)


class ApplicationPanelAssignment(BaseApplicationPanelAssignment):
    class Meta(BaseApplicationPanelAssignment.Meta):
        swappable = swapper.swappable_setting(
            BaseApplicationPanelAssignment.Meta.app_label,
            "ApplicationPanelAssignment")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_scenario_application import (
    BaseScenarioApplication
)


class ScenarioApplication(BaseScenarioApplication):
    class Meta(BaseScenarioApplication.Meta):
        swappable = swapper.swappable_setting(
            BaseScenarioApplication.Meta.app_label, "ScenarioApplication")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_scenario_preference import (
    BaseScenarioPreference
)


class ScenarioPreference(BaseScenarioPreference):
    class Meta(BaseScenarioPreference.Meta):
        swappable = swapper.swappable_setting(
            BaseScenarioPreference.Meta.app_label, "ScenarioPreference")

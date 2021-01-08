# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_scenario_preference import (
    BaseScenarioPreference
)


class ScenarioPreference(BaseScenarioPreference):
    class Meta(BaseScenarioPreference.Meta):
        swappable = False

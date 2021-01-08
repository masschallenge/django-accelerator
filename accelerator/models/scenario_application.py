# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_scenario_application import (
    BaseScenarioApplication
)


class ScenarioApplication(BaseScenarioApplication):
    class Meta(BaseScenarioApplication.Meta):
        swappable = False

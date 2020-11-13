# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_scenario import BaseScenario


class Scenario(BaseScenario):
    class Meta(BaseScenario.Meta):
        swappable = swapper.swappable_setting(
            BaseScenario.Meta.app_label, "Scenario")

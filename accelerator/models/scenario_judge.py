# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_scenario_judge import BaseScenarioJudge


class ScenarioJudge(BaseScenarioJudge):
    class Meta(BaseScenarioJudge.Meta):
        swappable = swapper.swappable_setting(
            BaseScenarioJudge.Meta.app_label, "ScenarioJudge")

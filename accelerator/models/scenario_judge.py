# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_scenario_judge import BaseScenarioJudge


class ScenarioJudge(BaseScenarioJudge):
    class Meta(BaseScenarioJudge.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_scenario import BaseScenario


class Scenario(BaseScenario):
    class Meta(BaseScenario.Meta):
        swappable = False

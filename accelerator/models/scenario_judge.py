# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.conf import settings
from django.db import models

from accelerator_abstract.models.base_scenario_judge import BaseScenarioJudge


class ScenarioJudge(BaseScenarioJudge):
    class Meta(BaseScenarioJudge.Meta):
        swappable = swapper.swappable_setting(
            BaseScenarioJudge.Meta.app_label, "ScenarioJudge")
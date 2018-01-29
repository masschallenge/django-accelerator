# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models

from accelerator_abstract.models.base_scenario_preference import BaseScenarioPreference


class ScenarioPreference(BaseScenarioPreference):
    class Meta(BaseScenarioPreference.Meta):
        swappable = swapper.swappable_setting(
            BaseScenarioPreference.Meta.app_label, "ScenarioPreference")
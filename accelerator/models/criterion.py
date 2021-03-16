# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_criterion import BaseCriterion


class Criterion(BaseCriterion):
    class Meta(BaseCriterion.Meta):
        swappable = swapper.swappable_setting(
            BaseCriterion.Meta.app_label, "Criterion")

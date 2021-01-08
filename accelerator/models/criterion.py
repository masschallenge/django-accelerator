# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_criterion import BaseCriterion


class Criterion(BaseCriterion):
    class Meta(BaseCriterion.Meta):
        swappable = False

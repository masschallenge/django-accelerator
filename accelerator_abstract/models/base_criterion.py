# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper

from django.db.models import (
    CharField,
    FloatField,
    ForeignKey,
    IntegerField,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel

DEFAULT_COUNT = 1
DEFAULT_WEIGHT = 1.0

class BaseCriterion(AcceleratorModel):
    type = CharField(max_length=64)
    name = CharField(max_length=64)
    count = IntegerField(default=DEFAULT_COUNT)
    weight = FloatField(default=DEFAULT_WEIGHT)
    judging_round = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgingRound"))

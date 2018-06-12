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


class BaseCriterion(AcceleratorModel):
    type = CharField(max_length=64)
    name = CharField(max_length=64)
    count = IntegerField()
    weight = FloatField()
    judging_round = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgingRound"))

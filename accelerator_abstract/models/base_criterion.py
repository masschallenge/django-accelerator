# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper

from django.db.models import (
    CharField,
    ForeignKey,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseCriterion(AcceleratorModel):

    type = CharField(max_length=64)
    name = CharField(max_length=64)
    judging_round = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgingRound"))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_criterion'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        return "Criterion: %s" % self.name

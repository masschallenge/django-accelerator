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


class BaseCriterionOptionSpec(AcceleratorModel):
    option = CharField(max_length=64)
    count = IntegerField()
    weight = FloatField()
    criterion = ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label,
        "Criterion"))
   
    
    

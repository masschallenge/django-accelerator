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
from accelerator_abstract.models.base_criterion import (
    DEFAULT_COUNT,
    DEFAULT_WEIGHT,
)

class BaseCriterionOptionSpec(AcceleratorModel):
    option = CharField(max_length=64)
    count = IntegerField(default=DEFAULT_COUNT)
    weight = FloatField(default=DEFAULT_WEIGHT)
    criterion = ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label,
        "Criterion"))
   
    
    

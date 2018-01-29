# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
@python_2_unicode_compatible
class BaseInterestCategory(AcceleratorModel):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=500, blank=True)
    program = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_interestcategory'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = "Interest Categories"

    def __str__(self):
        return self.name

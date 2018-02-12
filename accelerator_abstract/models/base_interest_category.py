# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseInterestCategory(AcceleratorModel):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=500, blank=True)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_interestcategory'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = "Interest Categories"


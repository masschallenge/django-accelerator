# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

VALID_EXPERT_CATEGORIES = [
    "Executive",
    "Investor",
    "Lawyer",
    "Other",
]


class BaseExpertCategory(AcceleratorModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_expertcategory'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ['name', ]
        verbose_name = "Expert Category"
        verbose_name_plural = "Expert Categories"

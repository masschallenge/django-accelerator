# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
from fluent_pages.models import Page


class BaseCategoryHeaderPage(Page, AcceleratorModel):
    is_category_header = models.BooleanField(default=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_categoryheaderpage'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Category Header"
        verbose_name_plural = "Category Headers"

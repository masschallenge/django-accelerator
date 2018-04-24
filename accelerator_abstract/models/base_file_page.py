# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from fluent_pages.models import Page

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseFilePage(Page):
    file = models.FileField(upload_to="%Y-%m")
    description = models.TextField(blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'pagetype_{}_filepage'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "File"
        verbose_name_plural = "Files"

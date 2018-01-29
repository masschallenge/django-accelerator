# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
from fluent_pages.models import Page


class BaseSiteRedirectPage(Page):
    new_url = models.CharField(max_length=100)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_siteredirectpage'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Site Redirect"
        verbose_name_plural = "Site Redirects"

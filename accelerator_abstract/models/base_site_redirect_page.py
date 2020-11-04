# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from fluent_pages.models import Page

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseSiteRedirectPage(Page):
    new_url = models.CharField(max_length=100)

    class Meta(AcceleratorModel.Meta):
        db_table = 'pagetype_{}_siteredirectpage'
        abstract = True
        verbose_name = "Site Redirect"
        verbose_name_plural = "Site Redirects"

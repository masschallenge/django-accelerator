from __future__ import unicode_literals

from django.db import models
from fluent_pages.models import Page

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseCategoryHeaderPage(Page):
    is_category_header = models.BooleanField(default=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'pagetype_accelerator_categoryheaderpage'
        abstract = True
        verbose_name = "Category Header"
        verbose_name_plural = "Category Headers"

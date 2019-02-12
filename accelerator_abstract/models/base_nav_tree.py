from __future__ import unicode_literals

from django.db import models

from sitetree.models import TreeBase

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseNavTree(TreeBase, AcceleratorModel):
    name = models.CharField(max_length=255)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_navtree'.format(AcceleratorModel.Meta.app_label)
        verbose_name_plural = "NavTrees"
        abstract = True

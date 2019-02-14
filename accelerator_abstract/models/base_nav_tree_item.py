from __future__ import unicode_literals

from django.db import models

import swapper

from sitetree.models import TreeItemBase

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseNavTreeItem(TreeItemBase, AcceleratorModel):
    name = models.CharField(max_length=255)
    tree = models.ForeignKey(to=swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "NavTree"))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_navtreeitem'.format(AcceleratorModel.Meta.app_label)
        verbose_name_plural = "NavTreeItems"
        abstract = True

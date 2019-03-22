from __future__ import unicode_literals

import swapper
from django.db import models
from sitetree.models import TreeItemBase

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseNavTreeItem(TreeItemBase, AcceleratorModel):
    """
    The tree field specifies the NavTree object that this item belongs to.
    The remaining fields of this model specify objects which are either
    allowed to access this item. In all cases, a null value implies
    "all programs"  For example, if the `program` field is null,
    then all programs are allowed to access this Item. If it is non-null,
    then only the selected programs are allowed to access it.
    """
    tree = models.ForeignKey(to=swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "NavTree"))
    user_role = models.ManyToManyField(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'UserRole'),
        blank=True)
    program_family = models.ManyToManyField(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'ProgramFamily'),
        blank=True)
    program = models.ManyToManyField(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'Program'),
        blank=True)
    active_program = models.BooleanField(default=False)
    display_single_item = models.BooleanField(default=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_navtreeitem'.format(AcceleratorModel.Meta.app_label)
        verbose_name_plural = "NavTreeItems"
        unique_together = ('tree', 'title', 'url')
        abstract = True

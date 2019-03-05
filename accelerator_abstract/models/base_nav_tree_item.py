from __future__ import unicode_literals

import swapper
from django.db import models
from sitetree.models import TreeItemBase

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseNavTreeItem(TreeItemBase, AcceleratorModel):
    """
    A class used to represent a django sitetree item

    Attributes
    ----------
    tree : obj
        the NavTree object that this item belongs to
    user_role : obj
        the UserRole allowed to access this tree item, a null
        here implies that we allow all UserRoles to access
        this item (default null)
    program_family : objs
        the ProgramFamilies allowed to access this tree item, a blank
        here implies that we allow all ProgramFamilies to access
        this item (default '')
    program : objs
        the Programs allowed to access this tree item, a blank
        here implies that we allow all Programs to access
        this item (default '')
    active_program : bool
        determines if the programs that access this item must be active
        (default False)
    program_exclude : int
        the Programs not allowed to access this tree item, a blank
        here implies that we don't exclude any Programs from accessing
        this item (default '')
    program_family_exclude : str
        the Programs not allowed to access this tree item, a blank
        here implies that we do not exclude any Programs from accessing
        this item (default '')
    """
    tree = models.ForeignKey(to=swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "NavTree"))
    user_role = models.ForeignKey(
        swapper.get_model_name(
            AcceleratorModel.Meta.app_label, "UserRole"),
        null=True,
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
    '''
        added to allow
         - 'show for all program families exluding program family Y'
         - 'show for program family X exluding program Y'
         - 'show to all programs exluding programs A, B, C'
        level filtering
    '''
    program_exclude = models.ManyToManyField(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'Program'),
        blank=True,
        related_name='program_exlusion')
    program_family_exclude = models.ManyToManyField(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'ProgramFamily'),
        blank=True,
        related_name='program_family_exlusion')

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_navtreeitem'.format(AcceleratorModel.Meta.app_label)
        verbose_name_plural = "NavTreeItems"
        abstract = True

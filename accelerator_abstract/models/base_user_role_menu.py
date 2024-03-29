from __future__ import unicode_literals

import swapper
from django.db import models
from fluent_pages.models import Page

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.models.base_nav_tree_item import NAV_TREE_USER_TYPES
from accelerator_abstract.models.base_program import PROGRAM_STATUSES


class BaseUserRoleMenu(Page):
    program_family = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramFamily"),
        verbose_name="Program Family",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        verbose_name="Program",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    user_role = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "UserRole"),
        verbose_name="User Role",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    program_status = models.CharField(
        max_length=64,
        choices=PROGRAM_STATUSES,
        null=True,
        blank=True,
    )
    user_type = models.CharField(
        max_length=12,
        choices=NAV_TREE_USER_TYPES,
        blank=True,
    )

    class Meta(AcceleratorModel.Meta):
        verbose_name = "User Role Menu"
        verbose_name_plural = "User Role Menus"
        db_table = 'pagetype_accelerator_userrolemenu'
        abstract = True

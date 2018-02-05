# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from fluent_pages.models import Page

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.models.base_program import PROGRAM_STATUSES


class BaseUserRoleMenu(AcceleratorModel, Page):
    program_family = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramFamily"),
        verbose_name="Program Family",
        blank=True,
        null=True)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        verbose_name="Program",
        blank=True,
        null=True)
    user_role = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "UserRole"),
        verbose_name="User Role",
        blank=True,
        null=True)
    program_status = models.CharField(
        max_length=64,
        choices=PROGRAM_STATUSES,
        null=True,
        blank=True,
    )

    class Meta(AcceleratorModel.Meta, Page.Meta):
        verbose_name = "User Role Menu"
        verbose_name_plural = "User Role Menus"
        db_table = '{}_userrolemenu'.format(AcceleratorModel.Meta.app_label)
        abstract = True

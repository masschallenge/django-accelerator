from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.models.label_model import LabelModel


class BaseProgramRole(LabelModel):
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        on_delete=models.CASCADE)
    name = models.CharField(max_length=LabelModel.LABEL_LENGTH,
                            unique=True,
                            db_index=True)
    user_role = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "UserRole"),
        null=True, blank=True, on_delete=models.CASCADE)
    landing_page = models.CharField(max_length=255, null=True, blank=True)
    newsletter_recipient = models.BooleanField(default=False)

    # March 10, 2016: This is a temporary mechanism to keep old
    # school ProgramRoleGrants in sync with shiny new UserLabels.
    # Going from ProgramRole to UserLabel is good.
    # Going from UserLabel to ProgramRole is bad.
    user_label = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "UserLabel"),
        blank=True,
        null=True,
        related_name="dont_use_commit_fail",
        on_delete=models.CASCADE)

    class Meta(LabelModel.Meta):
        db_table = 'accelerator_programrole'
        abstract = True
        ordering = ['name', ]
        verbose_name = "Program Role"
        verbose_name_plural = "Program Roles"

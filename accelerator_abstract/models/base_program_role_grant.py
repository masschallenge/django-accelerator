# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseProgramRoleGrant(AcceleratorModel):
    person = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    program_role = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "ProgramRole"),
        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_programrolegrant'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        unique_together = ('person', 'program_role')
        verbose_name = "Program Role Grant"
        verbose_name_plural = "Program Role Grants"

    def __str__(self):
        return "Role %s for %s" % (self.program_role, self.person)

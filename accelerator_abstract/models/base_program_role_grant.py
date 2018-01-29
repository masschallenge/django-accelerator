# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.conf import settings
from django.db import models


@python_2_unicode_compatible
class BaseProgramRoleGrant(AcceleratorModel):
    person = models.ForeignKey(settings.AUTH_USER_MODEL)
    program_role = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "ProgramRole"))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_programrolegrant'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        unique_together = ('person', 'program_role')
        verbose_name = "Program Role Grant"
        verbose_name_plural = "Program Role Grants"

    def __str__(self):
        return "Role %s for %s" % (self.program_role, self.person)

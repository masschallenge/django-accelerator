# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.conf import settings
from django.db import models

from accelerator_abstract.models.base_program_role_grant import BaseProgramRoleGrant


class ProgramRoleGrant(BaseProgramRoleGrant):
    person = models.ForeignKey(settings.AUTH_USER_MODEL)
    program_role = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramRoleGrant"))

    class Meta(BaseProgramRoleGrant.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramRoleGrant.Meta.app_label, "ProgramRoleGrant")

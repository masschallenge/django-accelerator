# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseStartupOverrideGrant(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=models.CASCADE)
    program_override = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramOverride"),
        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_startupoverridegrant'
        abstract = True
        verbose_name_plural = 'Startup Override Grants'

    def __str__(self):
        return ("Override grant (%s) for %s for %s" %
                (self.program_override.name,
                 self.startup.name,
                 self.program_override.program.name))

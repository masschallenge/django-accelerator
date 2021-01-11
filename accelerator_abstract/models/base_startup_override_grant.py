# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseStartupOverrideGrant(AcceleratorModel):
    startup = models.ForeignKey(
        "mc.Startup",
        on_delete=models.CASCADE)
    program_override = models.ForeignKey(
        "mc.ProgramOverride",
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

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseStartupStatus(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=models.CASCADE)
    program_startup_status = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramStartupStatus"),
        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_startupstatus'
        abstract = True
        verbose_name_plural = 'Startup Statuses'
        unique_together = ('startup', 'program_startup_status')

    def __str__(self):
        return "Startup Status (%s) for %s" % (
            self.program_startup_status.startup_status, self.startup.name)

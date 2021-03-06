from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseProgramFamilyLocation(AcceleratorModel):
    program_family = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramFamily"),
        on_delete=models.CASCADE)
    location = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "Location"),
        on_delete=models.CASCADE)
    primary = models.BooleanField()

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_programfamilylocation'
        abstract = True
        unique_together = ('program_family', 'location')
        verbose_name = "Program Family Location"
        verbose_name_plural = "Program Family Locations"

    def __str__(self):
        return "Location %s for %s" % (self.location, self.program_family)

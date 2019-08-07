from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseProgramFamilyLocation(AcceleratorModel):
    program_family = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramFamily"))
    location = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "Location"))
    primary = models.BooleanField()

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_programfamilylocation'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        unique_together = ('program_family', 'location')
        verbose_name = "Program Family Location"
        verbose_name_plural = "Program Family Locations"

    def __str__(self):
        return "Location %s for %s" % (self.location, self.program_family)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


from accelerator_abstract.models.accelerator_model import AcceleratorModel

CLEARANCE_LEVEL_EXEC_MD = "Exec/MD"
CLEARANCE_LEVEL_GLOBAL_MANAGER = "Global Manager"
CLEARANCE_LEVEL_POM = "Program Operations Manager"
CLEARANCE_LEVELS = [
    CLEARANCE_LEVEL_EXEC_MD,
    CLEARANCE_LEVEL_GLOBAL_MANAGER,
    CLEARANCE_LEVEL_POM,
]

CLEARANCE_LEVEL_CHOICES = [(x, x) for x in CLEARANCE_LEVELS]
CLEARANCE_FORMAT_STR = "Clearance {level} at {program_family} for {user}"


@python_2_unicode_compatible
class BaseClearance(AcceleratorModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=False,
                             blank=False,
                             related_name="clearances")
    level = models.CharField(choices=CLEARANCE_LEVEL_CHOICES,
                             null=False,
                             blank=False,
                             max_length=64)
    program_family = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "ProgramFamily"),
        null=False,
        blank=False,
        related_name="user_clearances")

    class Meta(AcceleratorModel.Meta):
        unique_together = ("user", "program_family")
        abstract = True
        db_table = "{}_clearance".format(
            AcceleratorModel.Meta.app_label)

    def __str__(self):
        return CLEARANCE_FORMAT_STR.format(level=self.level,
                                           program_family=self.program_family,
                                           user=self.user)

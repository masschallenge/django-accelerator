# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db.models import (
    ForeignKey,
    ManyToManyField,
    CASCADE,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseStartupCycleInterest(AcceleratorModel):
    cycle = ForeignKey(swapper.get_model_name('accelerator',
                                              "ProgramCycle"),
                       on_delete=CASCADE)
    startup = ForeignKey(
        swapper.get_model_name('accelerator', "Startup"),
        on_delete=CASCADE)
    interested_programs = ManyToManyField(
        swapper.get_model_name('accelerator', 'Program'),
        through=swapper.get_model_name('accelerator',
                                       'StartupProgramInterest'))

    class Meta(AcceleratorModel.Meta):
        unique_together = ('cycle', 'startup')
        db_table = 'accelerator_startupcycleinterest'
        abstract = True

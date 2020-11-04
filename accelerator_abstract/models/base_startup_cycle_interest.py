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
    cycle = ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                              "ProgramCycle"),
                       on_delete=CASCADE)
    startup = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=CASCADE)
    interested_programs = ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Program'),
        through=swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                       'StartupProgramInterest'))

    class Meta(AcceleratorModel.Meta):
        unique_together = ('cycle', 'startup')
        db_table = 'accelerator_startupcycleinterest'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

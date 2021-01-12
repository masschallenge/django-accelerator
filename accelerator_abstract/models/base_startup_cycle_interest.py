# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db.models import (
    ForeignKey,
    ManyToManyField,
    CASCADE,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseStartupCycleInterest(AcceleratorModel):
    cycle = ForeignKey("ProgramCycle",
                       on_delete=CASCADE)
    startup = ForeignKey(
        "Startup",
        on_delete=CASCADE)
    interested_programs = ManyToManyField(
        "Program",
        through="StartupProgramInterest")

    class Meta(AcceleratorModel.Meta):
        unique_together = ('cycle', 'startup')
        db_table = 'accelerator_startupcycleinterest'
        abstract = True

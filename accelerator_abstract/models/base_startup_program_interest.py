# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import logging

import swapper
from django.db import models
from ordered_model.models import OrderedModel

from accelerator_abstract.models.accelerator_model import AcceleratorModel

logger = logging.getLogger(__file__)

INTEREST_CHOICES = [
    ("g", "Definitely will participate"),
    ("w", "Will participate"),
    ("p", "Likely will participate"),
    ("n", "Might not participate"),
    ("l", "Likely won't participate"),
]
PROGRAM_INTEREST_BOTTOM = 'bottom'
PROGRAM_INTEREST_TOP = 'top'
PROGRAM_INTEREST_UP = 'up'
PROGRAM_INTEREST_DOWN = 'down'


class BaseStartupProgramInterest(OrderedModel, AcceleratorModel):
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        on_delete=models.CASCADE)
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=models.CASCADE)
    startup_cycle_interest = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "StartupCycleInterest"),
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    order_with_respect_to = 'startup_cycle_interest'
    applying = models.BooleanField(default=False)
    interest_level = models.CharField(
        max_length=64,
        choices=INTEREST_CHOICES,
        blank=True,
        null=True
    )

    class Meta(OrderedModel.Meta, AcceleratorModel.Meta):
        ordering = ['order']
        abstract = True
        db_table = 'accelerator_startupprograminterest'

    def __str__(self):
        return "{startup}-{program}, Applying:{applying}".format(
            startup=self.startup, program=self.program, applying=self.applying)

    def change_position(self, move):
        moves = {
            PROGRAM_INTEREST_UP: self.up,
            PROGRAM_INTEREST_DOWN: self.down,
            PROGRAM_INTEREST_TOP: self.top,
            PROGRAM_INTEREST_BOTTOM: self.bottom,
        }
        if move and move in moves.keys():
            moves[move]()

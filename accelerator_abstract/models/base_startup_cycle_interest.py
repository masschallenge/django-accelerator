# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db.models import (
    ForeignKey,
    ManyToManyField,
)


@python_2_unicode_compatible
class BaseStartupCycleInterest(AcceleratorModel):
    cycle = ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                              "ProgramCycle"))
    startup = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"))
    interested_programs = ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Program'),
        through=swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                       'StartupProgramInterest'))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_startupcycleinterest'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

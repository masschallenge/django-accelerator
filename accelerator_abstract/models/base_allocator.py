# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db.models import (
    CASCADE,
    OneToOneField,
)
from django.utils.encoding import python_2_unicode_compatible
from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseAllocator(AcceleratorModel):
    judging_round = OneToOneField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'JudgingRound'),
        on_delete=CASCADE,
        primary_key=True)
    scenario = OneToOneField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Scenario'),
        on_delete=CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_allocator'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Allocators'

    def __str__(self):
        return 'Allocator for %s' % str(self.judging_round)

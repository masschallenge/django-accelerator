from __future__ import unicode_literals

import swapper
from django.db.models import (
    CASCADE,
    OneToOneField,
)
from accelerator_abstract.models.accelerator_model import AcceleratorModel


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
        db_table = 'accelerator_allocator'
        abstract = True
        verbose_name_plural = 'Allocators'

    def __str__(self):
        return 'Allocator for %s' % str(self.judging_round)

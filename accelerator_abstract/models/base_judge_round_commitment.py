# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import logging

import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

logger = logging.getLogger(__file__)

NOT_AVAILABLE_MSG = ("You have indicated that you are not available for "
                     "this round.")


@python_2_unicode_compatible
class BaseJudgeRoundCommitment(AcceleratorModel):
    judge = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    judging_round = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgingRound"),
        on_delete=models.CASCADE)
    commitment_state = models.BooleanField(default=True)
    capacity = models.IntegerField(default=0)
    current_quota = models.IntegerField(blank=True, null=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_judgeroundcommitment'
        abstract = True
        verbose_name_plural = ("Judge commitment to participate in a "
                               "Judging Round")
        unique_together = ('judge', 'judging_round')

    def __str__(self):
        return "%s commited to %s" % (self.judge, self.judging_round)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseScenarioJudge(AcceleratorModel):
    judge = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    scenario = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Scenario"),
        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_scenariojudge'
        abstract = True
        verbose_name_plural = 'Scenario Judges'
        unique_together = ('scenario', 'judge')

    def __str__(self):
        return "%s in %s" % (self.judge, self.scenario)

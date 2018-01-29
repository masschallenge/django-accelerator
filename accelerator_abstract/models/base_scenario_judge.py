# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.conf import settings
from django.db import models

@python_2_unicode_compatible
class BaseScenarioJudge(AcceleratorModel):
    judge = models.ForeignKey(settings.AUTH_USER_MODEL)
    scenario = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "Scenario"))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_scenariojudge'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Scenario Judges'
        unique_together = ('scenario', 'judge')

    def __str__(self):
        return "%s in %s" % (self.judge, self.scenario)

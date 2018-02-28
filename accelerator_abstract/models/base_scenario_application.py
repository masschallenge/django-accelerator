# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseScenarioApplication(AcceleratorModel):
    application = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Application"))
    scenario = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Scenario"))
    # default 1. How much do we want this application assigned now?
    # Set higher for foreign and early bird.
    priority = models.IntegerField(default=1)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_scenarioapplication'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Scenario Applications'
        unique_together = ('scenario', 'application')

    def __str__(self):
        return "%s in %s" % (self.application, self.scenario)

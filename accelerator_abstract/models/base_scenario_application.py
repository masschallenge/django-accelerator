# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseScenarioApplication(AcceleratorModel):
    application = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Application"),
        on_delete=models.CASCADE)
    scenario = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Scenario"),
        on_delete=models.CASCADE)
    # default 1. How much do we want this application assigned now?
    # Set higher for foreign and early bird.
    priority = models.IntegerField(default=1)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_scenarioapplication'
        abstract = True
        verbose_name_plural = 'Scenario Applications'
        unique_together = ('scenario', 'application')

    def __str__(self):
        return "%s in %s" % (self.application, self.scenario)

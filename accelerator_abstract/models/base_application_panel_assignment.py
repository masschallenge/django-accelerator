# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseApplicationPanelAssignment(AcceleratorModel):
    application = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "Application"),
        on_delete=models.CASCADE)
    panel = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "Panel"),
        on_delete=models.CASCADE)
    scenario = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "Scenario"),
        related_name="application_assignments",
        on_delete=models.CASCADE
    )
    panel_slot_number = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    remote_pitch = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = "assignments of startup applications to panel"
        unique_together = ("application", "panel", "scenario")
        ordering = ('panel_slot_number',)
        db_table = '{}_applicationpanelassignment'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        tmpl = "%s -> %s"
        return tmpl % (self.application, self.panel)

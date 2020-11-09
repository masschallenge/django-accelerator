# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

ASSIGNED_PANEL_ASSIGNMENT_STATUS = "ASSIGNED"
COMPLETE_PANEL_ASSIGNMENT_STATUS = "COMPLETE"

JUDGE_PANEL_ASSIGNMENT_STATUS_ENUM = (
    (ASSIGNED_PANEL_ASSIGNMENT_STATUS, ASSIGNED_PANEL_ASSIGNMENT_STATUS),
    (COMPLETE_PANEL_ASSIGNMENT_STATUS, COMPLETE_PANEL_ASSIGNMENT_STATUS)
)


@python_2_unicode_compatible
class BaseJudgePanelAssignment(AcceleratorModel):
    judge = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    panel = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Panel"),
        on_delete=models.CASCADE)
    scenario = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Scenario"),
        related_name='judge_assignments',
        on_delete=models.CASCADE)
    assignment_status = models.CharField(
        choices=JUDGE_PANEL_ASSIGNMENT_STATUS_ENUM,
        max_length=16,
        blank=True,
        default="")
    panel_sequence_number = models.PositiveIntegerField(
        help_text="Indicate in which order this panel should be completed "
                  "by this judge",
        blank=True,
        null=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_judgepanelassignment'
        abstract = True
        verbose_name_plural = "assignments of judge to panel"
        unique_together = ('judge', 'panel', 'scenario')

    def __str__(self):
        tmpl = "%s -> %s"
        return tmpl % (self.judge, self.panel)

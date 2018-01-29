# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel

from django.conf import settings
from django.db.models import (
    CharField,
    ManyToManyField,
    ForeignKey,
)

ACTIVE_PANEL_STATUS = "ACTIVE"
COMPLETED_PANEL_STATUS = "COMPLETED"
DEFAULT_PANEL_STATUS = "NOT STARTED"
PREVIEW_PANEL_STATUS = "PREVIEW"
PANEL_STATUS_ENUM = ((DEFAULT_PANEL_STATUS, "NOT STARTED"),
                     (PREVIEW_PANEL_STATUS, "PREVIEW"),
                     (ACTIVE_PANEL_STATUS, "ACTIVE"),
                     (COMPLETED_PANEL_STATUS, "COMPLETED"),)

PANEL_AVAILABILITY_KEYWORD_SLOTS = {'time': 'panel_time',
                                    'type': 'panel_type',
                                    'location': 'location'}


@python_2_unicode_compatible
class BasePanel(AcceleratorModel):
    judges = ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="panels",
        through=swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                       'JudgePanelAssignment'))
    applications = ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Application'),
        related_name='panels',
        through=swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                       'ApplicationPanelAssignment')
    )
    panel_time = ForeignKey('PanelTime', blank=True, null=True)
    panel_type = ForeignKey('PanelType', blank=True, null=True)
    description = CharField(max_length=30, blank=True)
    location = ForeignKey('PanelLocation', blank=True, null=True)
    status = CharField(
        max_length=30,
        choices=PANEL_STATUS_ENUM,
        default=DEFAULT_PANEL_STATUS)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Panels'
        db_table = '{}_panel'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        if self.description:
            return self.description
        if self.panel_type and self.panel_time:
            return '{} panel: {} (ID {})'.format(
                self.panel_type, self.panel_time, self.pk)
        return 'Panel {}'.format(self.pk)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

PROGRAM_STARTUP_ATTRIBUTE_TYPES = (
    ('django.forms.CharField', 'Text Line'),
    ('django.forms.IntegerField', 'Integer'),
    ('django.forms.FloatField', 'Floating Point Value'),
    ('django.forms.BooleanField', 'True/False'),
)


@python_2_unicode_compatible
class BaseProgramStartupAttribute(AcceleratorModel):
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        on_delete=models.CASCADE)
    attribute_type = models.CharField(
        'Type',
        max_length=63,
        help_text='Select the type of information for this attribute',
        choices=PROGRAM_STARTUP_ATTRIBUTE_TYPES)
    attribute_label = models.CharField(
        'Label',
        max_length=127,
        help_text='Provide a human-readable label for this attribute.  '
                  'It must be unique for the selected Program')
    attribute_description = models.CharField(
        'Description',
        max_length=255,
        help_text='Provide "help text" for this attribute',
        blank=True)
    admin_viewable = models.BooleanField(
        default=False,
        help_text='Can Startup Administrators view this attribute for '
                  'their own Startups?')
    non_admin_viewable = models.BooleanField(
        default=False,
        help_text='Can Non-Startup Administrators view this attribute for '
                  'their own Startups?')
    staff_viewable = models.BooleanField(
        default=False,
        help_text='Can MC Staff view this attribute?')
    finalist_viewable = models.BooleanField(
        default=False,
        help_text='Can Other Finalists view this attribute?')
    mentor_viewable = models.BooleanField(
        default=False,
        help_text='Can Mentors view this attribute?')

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_programstartupattribute'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ['program', 'attribute_label']
        unique_together = ('program', 'attribute_label')

    def __str__(self):
        type_display = self.attribute_type_display()
        return '{} ({} attribute)'.format(self.attribute_label, type_display)

    def attribute_type_display(self):
        types_dict = dict(PROGRAM_STARTUP_ATTRIBUTE_TYPES)
        return types_dict.get(str(self.attribute_type), '')

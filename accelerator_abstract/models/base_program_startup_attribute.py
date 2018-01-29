# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import swapper

from django.db import models
from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.utils import (
    convert_to_integer,
    convert_from_integer,
    convert_to_float,
    convert_from_float,
    convert_to_boolean,
    convert_from_boolean,
)

PROGRAM_STARTUP_ATTRIBUTE_TYPES = (
    ('django.forms.CharField', 'Text Line'),
    ('django.forms.IntegerField', 'Integer'),
    ('django.forms.FloatField', 'Floating Point Value'),
    ('django.forms.BooleanField', 'True/False'),
)

# dict 'field_type': {'to_field': to_field_value, 'to_stored': to_stored_value}
ATTRIBUTE_TYPE_CONVERTERS = {
    'django.forms.CharField': {'to_field': None,
                               'to_stored': None},
    'django.forms.IntegerField': {'to_field': convert_to_integer,
                                  'to_stored': convert_from_integer},
    'django.forms.FloatField': {'to_field': convert_to_float,
                                'to_stored': convert_from_float},
    'django.forms.BooleanField': {'to_field': convert_to_boolean,
                                  'to_stored': convert_from_boolean},
}


@python_2_unicode_compatible
class BaseProgramStartupAttribute(AcceleratorModel):
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"))
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
        db_table = '{}_programstartupattribute'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ['program', 'attribute_label']
        unique_together = ('program', 'attribute_label')

    def __str__(self):
        tmpl = "%s (%s attribute)"
        return tmpl % (self.attribute_label, self.get_attribute_type_display())

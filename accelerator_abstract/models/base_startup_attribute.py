# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models


@python_2_unicode_compatible
class BaseStartupAttribute(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"))
    attribute = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramStartupAttribute"))
    # TextField allows me to ignore max_length.
    attribute_value = models.TextField(
        'Value',
        help_text='Stored text representation of the value')

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_startupattribute'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Startup Attributes'

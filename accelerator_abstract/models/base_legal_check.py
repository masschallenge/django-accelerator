# MIT License
# Copyright (c) 2017 MassChallenge, Inc.
# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseLegalCheck(AcceleratorModel):
    name = models.CharField(max_length=128,
                            default='',
                            null=False,
                            blank=False,
                            unique=True,
                            help_text='Internal name for this check.')
    description = models.TextField(
        help_text='Text displayed next to checkbox. Use HTML for links.')
    is_enabled_for_experts = models.BooleanField(
        default=True,
        help_text='This legal check is for Experts (Judges and Mentors)')
    is_enabled_for_entrepreneurs = models.BooleanField(
        default=True,
        help_text='This legal check is for Entrepreneurs (people with '
                  'Startups applying to MassChallenge)')

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_legalcheck'.format(AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Legal Check"

    def __str__(self):
        return 'Legal Check: {}'.format(self.name)

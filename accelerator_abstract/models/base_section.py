# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

ANY_SPECIFIED_CATEGORY = 'ANY_SPECIFIED_CATEGORY'

INCLUDE_FOR_CHOICES = (('EVERYONE', 'Everyone'),
                       (ANY_SPECIFIED_CATEGORY, 'Any specified category'))

SECTION_SEQUENCE_HELP = "specify the order of this section in the newsletter"


@python_2_unicode_compatible
class BaseSection(AcceleratorModel):
    heading = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    interest_categories = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'InterestCategory'),
        blank=True)
    include_for = models.CharField(
        max_length=32,
        choices=INCLUDE_FOR_CHOICES,
        default='EVERYONE')
    newsletter = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Newsletter"),
        related_name='sections', on_delete=models.CASCADE)
    sequence = models.PositiveIntegerField(help_text=SECTION_SEQUENCE_HELP)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_section'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ('newsletter', 'sequence',)

    def __str__(self):
        return self.heading

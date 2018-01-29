# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from sorl.thumbnail import ImageField

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BasePartner(AcceleratorModel):
    organization = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "Organization"), null=True, blank=True)
    description = models.TextField(
        max_length=1000,
        blank=True,
        help_text='This is the generic description of the Partner, shared '
                  'across all Programs.')
    partner_logo = ImageField(
        upload_to='startup_pics',
        verbose_name="Partner Logo",
        blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_partner'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Partners'
        ordering = ['organization__name', ]

    def __str__(self):
        return self.organization.name

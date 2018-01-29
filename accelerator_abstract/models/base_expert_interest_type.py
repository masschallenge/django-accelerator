# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseExpertInterestType(AcceleratorModel):
    """A category of involvement an expert has with a program or program family
    """
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=255)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_expertinteresttype'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = "Expert Interest Types"

    def __str__(self):
        return self.name

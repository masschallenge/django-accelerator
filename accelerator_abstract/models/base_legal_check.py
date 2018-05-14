# MIT License
# Copyright (c) 2017 MassChallenge, Inc.
# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseLegalCheck(AcceleratorModel):
    name = models.CharField(max_length=128,
                            default='',
                            null=False,
                            blank=False)
    profiles = models.ManyToManyField(
        to=swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                  "BaseProfile"))
    title = models.CharField(max_length=512,
                             default='',
                             null=False,
                             blank=False)
    url = models.URLField(max_length=100)
    accepted = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_legalcheck'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Legal Check"

    def __str__(self):
        return 'Legal Check: {}'.format(self.title)

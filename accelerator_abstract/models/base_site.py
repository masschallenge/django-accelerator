# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseSite(AcceleratorModel):
    name = models.CharField(max_length=50, unique=True)
    security_key = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    site_url = models.URLField(blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_site'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        return "{0} at {1}".format(self.name,
                                   self.site_url
                                   if self.site_url else "unknown url")

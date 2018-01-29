# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
@python_2_unicode_compatible
class BaseObserver(AcceleratorModel):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="Email address", max_length=100)
    title = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    newsletter_cc_roles = models.ManyToManyField(swapper.get_model_name(AcceleratorModel.Meta.app_label, 'ProgramRole'),
        blank=True)
    newsletter_sender = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_observer'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ['last_name', 'first_name']
        verbose_name = "Observer"
        verbose_name_plural = "Observers"

    def __str__(self):
        if self.first_name:
            full_name = "%s, %s" % (self.last_name, self.first_name)
        else:
            full_name = self.last_name
        return "%s (%s)" % (full_name, self.email)

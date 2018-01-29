# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from mptt.models import (
    MPTTModel,
    TreeForeignKey,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseIndustry(MPTTModel, AcceleratorModel):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=50, blank=True)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name="children")

    class MPTTMeta:
        order_insertion_by = ['name', ]
        verbose_name_plural = 'Industries'

    class Meta:
        db_table = '{}_industry'.format(AcceleratorModel.Meta.app_label)
        verbose_name_plural = "Industries"
        abstract = True

    def __str__(self):
        parent_name = ''
        if self.parent:
            parent_name = "%s - " % self.parent.name
        return "%s%s" % (parent_name, self.name)

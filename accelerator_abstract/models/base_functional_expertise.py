# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from mptt.models import (
    MPTTModel,
    TreeForeignKey,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseFunctionalExpertise(MPTTModel, AcceleratorModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name="children",
                            on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name', ]

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_functionalexpertise'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        parent_name = ''
        if self.parent:
            parent_name = "%s : " % str(self.parent)

        return "%s%s" % (parent_name, self.name)

from __future__ import unicode_literals

from django.db import models
from mptt.models import (
    MPTTModel,
    TreeForeignKey,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseIndustry(MPTTModel, AcceleratorModel):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=50, blank=True)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name="children",
                            on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name', ]
        verbose_name_plural = 'Industries'

    class Meta:
        db_table = 'accelerator_industry'
        verbose_name_plural = "Industries"
        abstract = True

    def __str__(self):
        parent_name = ''
        if self.parent:
            parent_name = "%s - " % self.parent.name
        return "%s%s" % (parent_name, self.name)

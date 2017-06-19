from django.conf import settings
from django.db import models

from mptt.models import (
    MPTTModel,
    TreeForeignKey,
)


@python_2_unicode_compatible
class Industry(models.Model):
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
        db_table = 'mc_industry'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        verbose_name_plural = "Industries"

    def __str__(self):
        parent_name = ''
        if self.parent:
            parent_name = "%s - " % self.parent.name
        return "%s%s" % (parent_name, self.name)

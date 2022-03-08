from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

VALID_EXPERT_CATEGORIES = [
    "Executive",
    "Investor",
    "Lawyer",
    "Entrepreneur",
    "Subject Matter Expert",    
    "Other",
]


class BaseExpertCategory(AcceleratorModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_expertcategory'
        abstract = True
        ordering = ['name', ]
        verbose_name = "Expert Category"
        verbose_name_plural = "Expert Categories"

from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseExpertInterestType(AcceleratorModel):
    """A category of involvement an expert has with a program or program family
    """
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=255)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_expertinteresttype'
        abstract = True
        verbose_name_plural = "Expert Interest Types"

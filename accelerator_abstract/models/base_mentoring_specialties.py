# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseMentoringSpecialties(AcceleratorModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_mentoringspecialties'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ['name', ]
        verbose_name = "Mentoring Specialty"
        verbose_name_plural = "Mentoring Specialties"


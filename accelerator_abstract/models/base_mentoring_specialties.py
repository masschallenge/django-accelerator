# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseMentoringSpecialties(AcceleratorModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_mentoringspecialties'
        abstract = True
        ordering = ['name', ]
        verbose_name = "Mentoring Specialty"
        verbose_name_plural = "Mentoring Specialties"

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

GENDER_MALE_CHOICE = "Male"
GENDER_FEMALE_CHOICE = "Female"
GENDER_CISGENDER_CHOICE = "Cisgender"
GENDER_TRANSGENDER_CHOICE = "Transgender"
GENDER_NON_BINARY_CHOICE = "Non-Binary"
GENDER_PREFER_TO_SELF_DESCRIBE_CHOICE = "I Prefer To Self-describe"
GENDER_PREFER_NOT_TO_SAY_CHOICE = "I Prefer Not To Say"

GENDER_CHOICES = (
    GENDER_MALE_CHOICE,
    GENDER_FEMALE_CHOICE,
    GENDER_CISGENDER_CHOICE,
    GENDER_TRANSGENDER_CHOICE,
    GENDER_NON_BINARY_CHOICE,
    GENDER_PREFER_TO_SELF_DESCRIBE_CHOICE,
    GENDER_PREFER_NOT_TO_SAY_CHOICE
)


class BaseGenderChoices(AcceleratorModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_genderchoices'
        abstract = True
        ordering = ['name', ]
        verbose_name = "Gender Choice"
        verbose_name_plural = "Gender Choices"

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import (
    RegexValidator,
    validate_slug
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseOrganization(AcceleratorModel):
    name = models.CharField(max_length=255)
    website_url = models.URLField(max_length=100, blank=True)
    twitter_handle = models.CharField(
        max_length=40,
        blank=True,
        help_text='Omit the "@". We\'ll add it.')
    public_inquiry_email = models.EmailField(verbose_name="Email address",
                                             max_length=100,
                                             blank=True)
    url_slug = models.CharField(
        max_length=64,
        blank=True,
        default="",  # This actually gets replaced by a real slug.
        unique=True,
        validators=[RegexValidator(".*\D.*",
                                   "Slug must contain a non-numeral."),
                    validate_slug, ]
    )

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_organization'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        verbose_name_plural = 'Organizations'
        ordering = ['name', ]
        abstract = True

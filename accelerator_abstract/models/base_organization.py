# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import slugify

from accelerator_abstract.models.accelerator_model import AcceleratorModel

STARTUP_TYPE = "startup"
PARTNER_TYPE = "partner"


class BaseOrganization(AcceleratorModel):
    name = models.CharField(max_length=255)
    website_url = models.URLField(
        max_length=100,
        blank=True,
        verbose_name="Website URL")
    twitter_handle = models.CharField(
        max_length=40,
        blank=True,
        help_text='Omit the "@". We\'ll add it.',
        verbose_name="Twitter handle")
    public_inquiry_email = models.EmailField(verbose_name="Email address",
                                             max_length=100,
                                             blank=True)
    url_slug = models.CharField(
        max_length=64,
        blank=True,
        default="",  # This actually gets replaced by a real slug.
        unique=True,
        validators=[
            RegexValidator(regex="^[\w-]+$",
                           message="Letters, numbers, and dashes only.")
        ]
    )

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_organization'
        verbose_name_plural = 'Organizations'
        ordering = ['name', ]
        abstract = True

    def save(self, *args, **kwargs):
        if self.url_slug == "":
            self.url_slug = slug_from_instance(self)
        super(BaseOrganization, self).save(*args, **kwargs)


def slug_from_instance(organization):
    slug = slugify(organization.name)
    if slug == "":
        slug = "organization"
    slug = slug[:61]
    slugbase = slug
    i = 0
    while (organization._meta.model.objects.filter(
            url_slug=slug).exists() and
           (i < 100 or slugbase == "organization")):
        i += 1
        slug = slugbase + "-" + str(i)
    return slug

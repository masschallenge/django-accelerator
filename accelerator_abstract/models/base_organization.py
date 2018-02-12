# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify

from accelerator_abstract.models.accelerator_model import AcceleratorModel

STARTUP_TYPE = "startup"
PARTNER_TYPE = "partner"


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
        validators=[
            RegexValidator(regex="^[\w-]+$",
                           message="Letters, numbers, and dashes only.")
        ]
    )

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_organization'.format(AcceleratorModel.Meta.app_label)
        verbose_name_plural = 'Organizations'
        ordering = ['name', ]
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.url_slug == "":
            self.url_slug = self.slug_from_instance()
        super(BaseOrganization, self).save(*args, **kwargs)

    def slug_from_instance(self):
        slug = slugify(self.name)
        if slug == "":
            slug = "organization"
        slug = slug[:61]
        slugbase = slug
        i = 0
        while (self._meta.model.objects.filter(
                url_slug=slug).exists() and
               (i < 100 or slugbase == "organization")):
            i += 1
            slug = slugbase + "-" + str(i)
        return slug

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper
from accelerator_abstract.models import BaseOrganization
from django.conf import settings
from django.template.defaultfilters import slugify


class Organization(BaseOrganization):
    class Meta:
        db_table = 'accelerator_organization'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        verbose_name_plural = 'Organizations'
        ordering = ['name', ]
        swappable = swapper.swappable_setting('accelerator',
                                              'Organization')
        abstract = False

    @classmethod
    def slug_from_instance(cls, instance):  # todo: move back to BaseOrganization
        slug = slugify(instance.name)
        if slug == "":
            slug = "organization"
        slug = slug[:61]
        slugbase = slug
        i = 0
        while (cls.objects.filter(url_slug=slug).exists() and
                   (i < 100 or slugbase == "organization")):
            i += 1
            slug = slugbase + "-" + str(i)
        return slug

    def save(self, *args, **kwargs):
        if self.url_slug == "":
            self.url_slug = Organization.slug_from_instance(self)
        super(Organization, self).save(*args, **kwargs)

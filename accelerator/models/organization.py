# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.template.defaultfilters import slugify

from accelerator_abstract.models import BaseOrganization


class Organization(BaseOrganization):
    class Meta(BaseOrganization.Meta):
        swappable = swapper.swappable_setting(BaseOrganization.Meta.app_label,
                                              'Organization')

    @classmethod
    def slug_from_instance(cls, instance):
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

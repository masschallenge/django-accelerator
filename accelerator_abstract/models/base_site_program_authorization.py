# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
@python_2_unicode_compatible
class BaseSiteProgramAuthorization(AcceleratorModel):
    site = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "Site"))
    program = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"))
    startup_profile_base_url = models.URLField()
    sponsor_profile_base_url = models.URLField()
    video_base_url = models.URLField()

    startup_list = models.BooleanField(default=False)
    startup_profiles = models.BooleanField(default=False)
    startup_team_members = models.BooleanField(default=False)
    mentor_list = models.BooleanField(default=False)
    videos = models.BooleanField(default=False)
    sponsor_list = models.BooleanField(default=False)
    sponsor_profiles = models.BooleanField(default=False)
    sponsor_logos = models.BooleanField(default=False)
    jobs = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_siteprogramauthorization'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        unique_together = (("site", "program"), )
        verbose_name_plural = 'Site Program Authorizations'

    def __str__(self):
        attrs = ['startup_list',
                 'startup_profiles',
                 'mentor_list',
                 'videos',
                 'sponsor_list',
                 'sponsor_profiles',
                 'sponsor_logos',
                 'jobs', ]
        return "{0} authorized on {1} to {2}".format(
            self.site.name,
            self.program.name,
            ', '.join([attr for attr in attrs if getattr(self, attr)]))

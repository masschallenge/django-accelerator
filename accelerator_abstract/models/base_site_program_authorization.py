from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseSiteProgramAuthorization(AcceleratorModel):
    site = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Site"),
        on_delete=models.CASCADE)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        on_delete=models.CASCADE)
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
        db_table = 'accelerator_siteprogramauthorization'
        abstract = True
        unique_together = (("site", "program"),)
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

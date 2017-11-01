# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel
import swapper

JOB_TYPE_VALUES = (('NONE', 'None'),
                   ('INTERNSHIP', 'An internship'),
                   ('PART_TIME_PERMANENT', 'A part-time permanent position'),
                   ('FULL_TIME_PERMANENT', 'A full-time permanent position'),
                   ('PART_TIME_CONTRACT', 'A part-time contract position'),
                   ('FULL_TIME_CONTRACT', 'A full-time contract position'))


@python_2_unicode_compatible
class BaseJobPosting(AcceleratorModel):
    startup = models.ForeignKey(swapper.get_model_name(
        "accelerator", "Startup"))
    postdate = models.DateTimeField(blank=False)
    type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_VALUES)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    applicationemail = models.EmailField(verbose_name="Email address",
                                         max_length=100, null=True, blank=True)
    more_info_url = models.URLField(max_length=100, null=True, blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_jobposting'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        verbose_name_plural = 'Job postings for startups'
        abstract = True

    def __str__(self):
        return "%s at %s" % (self.title, self.startup.organization.name)

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

MENTOR_HELP = ("Select the Mentors you would like to work with during "
               "the program. Start typing a Mentor's name; if they "
               "are in the Mentor Directory, their name should appear"
               " as you type. If you don't find the person you are "
               "looking for, use 'Other Mentors' below.")

ADDITIONAL_MENTORS_HELP = ("Add any mentors you meet with who are not"
                           " listed in the MassChallenge Mentor "
                           "Directory. Please provide their name, "
                           "company, and email address below.")

PROGRAM_GOALS_HELP = ("Submit the three goals you plan to work on "
                      "with your mentors during the accelerator program.")


@python_2_unicode_compatible
class BaseStartupMentorTrackingRecord(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=models.CASCADE)
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        on_delete=models.CASCADE)
    mentors = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     verbose_name="Registered Mentors",
                                     help_text=MENTOR_HELP,
                                     through='StartupMentorRelationship')
    other_mentors = models.TextField(
        verbose_name="Additional Mentors",
        help_text=ADDITIONAL_MENTORS_HELP,
        blank=True,
        null=True)
    notes = models.TextField(
        verbose_name="Program Goals",
        help_text=PROGRAM_GOALS_HELP,
        blank=True,
        null=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_startupmentortrackingrecord'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Mentor Tracking Record"
        verbose_name_plural = "Mentor Tracking Records"
        unique_together = ('startup', 'program',)

    def __str__(self):
        return "Mentor tracking record for %s" % self.startup.name

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

HOUR_IS_PAST_MESSAGE = "This office hour is in the past"
HOUR_HAS_BEEN_CANCELED_MESSAGE = "This office hour has been canceled"
HOUR_NOT_SPECIFIED_MESSAGE = "Office hour has not been specified"
HOUR_OWNED_BY_ANOTHER_MESSAGE = "This office hour is owned by another user"


@python_2_unicode_compatible
class BaseMentorProgramOfficeHour(AcceleratorModel):
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"))
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='mentor_officehours')
    finalist = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 verbose_name="Finalist",
                                 blank=True,
                                 null=True,
                                 related_name='finalist_officehours')
    start_date_time = models.DateTimeField(db_index=True)
    end_date_time = models.DateTimeField(db_index=True)
    description = models.TextField(blank=True)
    location = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Location"),
        null=True,
        blank=True)
    notify_reservation = models.BooleanField(default=True)
    topics = models.CharField(max_length=500, blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_mentorprogramofficehour'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Office Hour"
        unique_together = ('program', 'mentor', 'start_date_time')
        ordering = ['start_date_time']

    def __str__(self):
        hour_type = "Reserved"
        if self.is_open():
            hour_type = "Open"
        return "%s office hour with %s" % (hour_type, self.mentor)

    def is_open(self):
        return not bool(self.finalist)

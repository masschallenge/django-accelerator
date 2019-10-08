# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

ACTIVE_PROGRAM_STATUS = "active"
ENDED_PROGRAM_STATUS = "ended"
HIDDEN_PROGRAM_STATUS = "hidden"
UPCOMING_PROGRAM_STATUS = "upcoming"
PROGRAM_STATUSES = ((UPCOMING_PROGRAM_STATUS, 'Upcoming'),
                    (ACTIVE_PROGRAM_STATUS, 'Active'),
                    (ENDED_PROGRAM_STATUS, 'Ended'),
                    (HIDDEN_PROGRAM_STATUS, 'Hidden'))
CURRENT_STATUSES = [ACTIVE_PROGRAM_STATUS, UPCOMING_PROGRAM_STATUS]

REFUND_CODES_DISABLED = "disabled"
REFUND_CODES_ENABLED = "enabled"
REFUND_CODES_VIEW_ONLY = "view-submitted-only"

REFUND_CODE_SUPPORT_VALUES = (
    (REFUND_CODES_ENABLED, "Enabled"),
    (REFUND_CODES_VIEW_ONLY, "View Submitted Only"),
    (REFUND_CODES_DISABLED, "Disabled"),
)
INVALID_OVERVIEW_DEADLINE_MSG = ("Overview deadline date must be set"
                                 " if start date is set")
INVALID_OVERVIEW_START_MSG = ("Overview start date must be set"
                              " if deadline date is set")
INVALID_OVERVIEW_TIMESPAN_MSG = ("Overview deadline date must be"
                                 " after start date")


class BaseProgram(AcceleratorModel):
    """An Accelerator program"""
    name = models.CharField(max_length=50)
    program_family = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramFamily"),
        related_name="programs",
    )
    cycle = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramCycle"),
        blank=True,
        null=True,
        related_name="programs")
    description = models.CharField(max_length=500, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=50,
                                blank=True,
                                null=True)
    program_status = models.CharField(
        max_length=64,
        choices=PROGRAM_STATUSES,
    )
    alumni_eligible_program = models.BooleanField(
        default=False,
        help_text=('Finalists will be added to our Global ' +
                   'Alumni Program upon this program being set to "Ended"')
    )
    currency_code = models.CharField(max_length=3)
    early_application_fee = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )
    regular_application_fee = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )
    regular_fee_suffix = models.CharField(max_length=20, blank=True)
    interested_judge_message = models.TextField(
        blank=True,
        help_text="You may use HTML, including links"
    )
    approved_judge_message = models.TextField(
        blank=True,
        help_text="You may use HTML, including links")
    interested_mentor_message = models.TextField(
        blank=True,
        help_text="You may use HTML, including links"
    )
    approved_mentor_message = models.TextField(
        blank=True,
        help_text="You may use HTML, including links")
    interested_speaker_message = models.TextField(
        blank=True,
        help_text="You may use HTML, including links"
    )
    approved_speaker_message = models.TextField(
        blank=True,
        help_text="You may use HTML, including links")
    interested_office_hours_message = models.TextField(
        blank=True,
        help_text="You may use HTML, including links"
    )
    approved_office_hours_message = models.TextField(
        blank=True,
        help_text="You may use HTML, including links")
    refund_code_support = models.CharField(
        max_length=64,
        choices=REFUND_CODE_SUPPORT_VALUES,
        default='enabled',
    )
    many_codes_per_partner = models.BooleanField(
        default=False,
        verbose_name="Allow multiple refund codes per partner",
        help_text=u"If true, then a given application may apply more than one "
                  u"refund code from the same partner for this program"
    )
    url_slug = models.CharField(
        max_length=30,
        default="",
    )
    accepting_mentors_and_goals = models.BooleanField(default=False)
    mentor_program_group = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "NamedGroup"),
        blank=True,
        null=True)
    overview_start_date = models.DateTimeField(
        blank=True, null=True,
        help_text="Time is in UTC")
    overview_deadline_date = models.DateTimeField(
        blank=True, null=True,
        help_text="Time is in UTC")
    eventbrite_organizer_id = models.CharField(
        max_length=20,
        blank=True,
        null=True)
    program_overview_link = models.URLField(
        blank=True,
        null=True,
        max_length=255,
        help_text=('URL of the program overview page, '
                   'ex: https://masschallenge.org/programs-boston')
        )

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Programs'
        abstract = True
        db_table = '{}_program'.format(AcceleratorModel.Meta.app_label)

    def family_abbr(self):
        return self.program_family.url_slug.upper()

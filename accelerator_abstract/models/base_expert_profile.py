# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import decimal

import swapper
from django.db import models

from accelerator_abstract.models.base_core_profile import BaseCoreProfile

INVITED_JUDGE_ALERT = (
    "<h4>{first_name}, we would like to invite you to be a judge at "
    "MassChallenge!</h4>"
    "<p>&nbsp;</p>"
    "<p>{round_name} judging occurs from {start_date} to {end_date}! "
    "Of all our potential judges, we would like you, {first_name}, "
    "to take part."
    "</p><p>&nbsp;</p>"
    '<p><a class="btn btn-primary" href="/expert/commitments/">Click '
    "here to tell us your availability"
    "</a></p> <p>&nbsp;</p>"
)

MENTOR_TYPE_HELPTEXT = (
    "Allowed Values: "
    "F - Functional Expert, "
    "P - Partner, "
    "T - Technical, "
    "E - Entrepreneur, "
    "N - Once accepted, now rejected, "
    "X - Not Accepted as a Mentor (may still be a judge)")

JUDGE_TYPE_HELPTEXT = (
    "Allowed Values: "
    "1 - Round 1 Judge, "
    "2 - Round 2 Judge, "
    "3 - Pre-final Judge, "
    "4 - Final Judge, "
    "0 - Once Accepted, now rejected, "
    "X - Not Accepted as a Judge (May still be a mentor)")


class BaseExpertProfile(BaseCoreProfile):
    user_type = 'expert'
    default_page = "expert_homepage"
    salutation = models.CharField(
        max_length=255,
        blank=True)
    mentor_type = models.CharField(
        max_length=1,
        blank=True,
        help_text=MENTOR_TYPE_HELPTEXT,
        verbose_name="Mentor Type")
    judge_type = models.CharField(
        max_length=1,
        blank=True,
        help_text=JUDGE_TYPE_HELPTEXT,
        verbose_name="Judge Type")
    public_website_consent_checked = models.BooleanField(
        verbose_name="Public Website Consent Check",
        blank=False,
        null=False,
        default=False)
    mentoring_specialties = models.ManyToManyField(
        swapper.get_model_name(BaseCoreProfile.Meta.app_label,
                               'MentoringSpecialties'),
        verbose_name="Mentoring Specialties",
        help_text='Hold down "Control", or "Command" on a Mac,'
                  'to select more than one.',
        db_table="accelerator_expert_related_mentoringspecialty",
        related_name="experts",
        blank=True)
    expert_group = models.CharField(
        verbose_name="Expert Group",
        max_length=10,
        blank=True)
    reliability = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=decimal.Decimal("1.00"),
        blank=True,
        null=True)
    internal_notes = models.TextField(
        max_length=500,
        blank=True,
        help_text="Internal notes only for use by MassChallenge Staff "
                  "(not visible to Expert)")

    class Meta(BaseCoreProfile.Meta):
        db_table = 'accelerator_expertprofile'
        abstract = True
        permissions = (
            ('change_password', 'Can change users passwords directly'),
        )

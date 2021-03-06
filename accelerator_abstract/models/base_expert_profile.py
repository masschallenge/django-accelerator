# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import decimal

import swapper
from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe

from accelerator_abstract.models.base_core_profile import BaseCoreProfile

PRIVACY_CHOICES = (("staff", "MC Staff Only"),
                   ("finalists and staff", "Finalists and MC Staff"),
                   ("public", "All Users"),)

BASE_INTEREST = "I would like to participate in MassChallenge %s"

BASE_TOPIC = ("Please describe the topic(s) you would be available "
              "to speak%s about%s")

REF_BY_TEXT = ("If someone referred you to MassChallenge, please provide "
               "their name (and organization if relevant). Otherwise, please "
               "indicate how you learned about the opportunity to participate "
               "at MassChallenge (helps us understand the effectiveness of "
               "our outreach programs).")

OTHER_EXPERTS_TEXT = ("We're always looking for more great experts to join "
                      "the MassChallenge community and program. We welcome "
                      "the names and contact info (email) of individuals you "
                      "think could be great additions to the program, as well "
                      "as how you think they might want to be involved "
                      "(Judge, Mentor, etc.) Also, please encourage these "
                      "individuals to fill out their own Expert Profile.")

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

BIO_MAX_LENGTH = 7500

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
    title = models.CharField(
        max_length=255,
        verbose_name="Professional Title")
    company = models.CharField(
        max_length=255,
        verbose_name="Company Name")
    expert_category = models.ForeignKey(
        swapper.get_model_name(BaseCoreProfile.Meta.app_label,
                               "ExpertCategory"),
        verbose_name="I primarily consider myself a(n)",
        related_name="experts",
        on_delete=models.CASCADE)
    functional_expertise = models.ManyToManyField(
        swapper.get_model_name(BaseCoreProfile.Meta.app_label,
                               'FunctionalExpertise'),
        verbose_name="Functional Expertise",
        related_name="experts",
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
    primary_industry = models.ForeignKey(
        settings.MPTT_SWAPPABLE_INDUSTRY_MODEL,
        verbose_name="Primary Industry",
        related_name="experts",
        limit_choices_to={'level__exact': 0},
        null=True,
        on_delete=models.CASCADE)
    additional_industries = models.ManyToManyField(
        settings.MPTT_SWAPPABLE_INDUSTRY_MODEL,
        verbose_name="Additional Industries",
        help_text=(mark_safe(
            'You may select up to 5 related industries. To select multiple '
            'industries, please press and hold Control (CTRL) on PCs or '
            'Command (&#8984;) on Macs.')),
        related_name="secondary_experts",
        db_table="accelerator_expert_related_industry")
    privacy_email = models.CharField(
        max_length=64,
        verbose_name="Privacy - Email",
        choices=PRIVACY_CHOICES,
        default=PRIVACY_CHOICES[1][0])
    privacy_phone = models.CharField(
        max_length=64,
        verbose_name="Privacy - Phone",
        choices=PRIVACY_CHOICES,
        default=PRIVACY_CHOICES[1][0])
    privacy_web = models.CharField(
        max_length=64,
        verbose_name="Privacy - Web",
        choices=PRIVACY_CHOICES,
        default=PRIVACY_CHOICES[1][0])
    public_website_consent = models.BooleanField(
        verbose_name="Public Website Consent",
        blank=False,
        null=False,
        default=False)
    public_website_consent_checked = models.BooleanField(
        verbose_name="Public Website Consent Check",
        blank=False,
        null=False,
        default=False)
    judge_interest = models.BooleanField(
        verbose_name="Judge",
        help_text=BASE_INTEREST % 'as a Judge',
        default=False)
    mentor_interest = models.BooleanField(
        verbose_name="Mentor",
        help_text=BASE_INTEREST % 'as a Mentor',
        default=False)
    speaker_interest = models.BooleanField(
        verbose_name="Speaker",
        help_text=BASE_INTEREST % 'as a Speaker',
        default=False)
    speaker_topics = models.TextField(
        verbose_name="Speaker Topics",
        help_text=BASE_TOPIC % ('', ''),
        blank=True)
    office_hours_interest = models.BooleanField(
        verbose_name="Office Hours",
        help_text=BASE_INTEREST % 'by holding Office Hours',
        default=False)
    office_hours_topics = models.TextField(
        verbose_name="Office Hour Topics",
        help_text=BASE_TOPIC % (' to Finalists', ' during Office Hours'),
        blank=True)
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
    referred_by = models.TextField(
        max_length=500,
        blank=True,
        help_text=REF_BY_TEXT)
    other_potential_experts = models.TextField(
        max_length=500,
        blank=True,
        help_text=OTHER_EXPERTS_TEXT)
    internal_notes = models.TextField(
        max_length=500,
        blank=True,
        help_text="Internal notes only for use by MassChallenge Staff "
                  "(not visible to Expert)")
    home_program_family = models.ForeignKey(
        swapper.get_model_name(BaseCoreProfile.Meta.app_label,
                               "ProgramFamily"),
        verbose_name="Home Program Family",
        blank=False,
        null=False,
        on_delete=models.CASCADE)

    class Meta(BaseCoreProfile.Meta):
        db_table = 'accelerator_expertprofile'
        abstract = True
        permissions = (
            ('change_password', 'Can change users passwords directly'),
        )

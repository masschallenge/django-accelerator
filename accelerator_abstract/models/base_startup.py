# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import logging

import swapper
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.models.base_startup_role import BaseStartupRole

logger = logging.getLogger(__name__)

DEFAULT_PROFILE_BACKGROUND_COLOR = '217181'  # default dark blue

DEFAULT_PROFILE_TEXT_COLOR = 'FFFFFF'

STARTUP_COMMUNITIES = (
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
)
STARTUP_NO_ORG_WARNING_MSG = "Startup {} has no organization"
DISPLAY_STARTUP_STATUS = "{status} {year} ({program_family_slug})"


class BaseStartup(AcceleratorModel):
    organization = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, 'Organization'), blank=True,
        null=True, related_name='startups', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_visible = models.BooleanField(
        default=True,
        help_text=('Startup Profiles will be published to external websites '
                   'through the the API.'))
    primary_industry = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Industry'),
        verbose_name='Primary Industry categorization',
        related_name='startups', on_delete=models.CASCADE)
    additional_industries = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Industry'),
        verbose_name='Additional Industries',
        related_name='secondary_startups',
        db_table="accelerator_startup_related_industry",
        blank=True,
        help_text=(
            'You may select up to 5 related industries.'
        ),
    )
    short_pitch = models.CharField(
        max_length=140,
        blank=False,
        help_text='Your startup in 140 characters or less.')
    full_elevator_pitch = models.TextField(
        max_length=500,
        blank=False,
        help_text='Your startup in 500 characters or less.')
    linked_in_url = models.URLField(
        blank=True,
        max_length=100,
        verbose_name="LinkedIn profile URL")
    facebook_url = models.URLField(
        blank=True,
        max_length=100,
        verbose_name="Facebook profile URL")
    high_resolution_logo = ImageField(
        upload_to='startup_pics',
        verbose_name='High Resolution Logo',
        blank=True)
    video_elevator_pitch_url = EmbedVideoField(
        max_length=100,
        blank=True,
        help_text=(
            'Upload your 1-3 minute video pitch to Vimeo or Youtube. '
            'Paste the shared link here.')
    )

    acknowledgement = models.BooleanField(
        default=False,
        help_text=(
            'I understand that my Startup Profile is a pre-requisite '
            'for applying to any MassChallenge Program'
        )
    )

    created_datetime = models.DateTimeField(blank=True, null=True)
    last_updated_datetime = models.DateTimeField(blank=True, null=True)
    community = models.CharField(
        max_length=64,
        choices=STARTUP_COMMUNITIES,
        blank=True,
    )

    # profile color fields are deprecated - do not delete until we know
    # what the marketing site is doing with startup display

    profile_background_color = models.CharField(
        max_length=7,
        blank=True,
        default=DEFAULT_PROFILE_BACKGROUND_COLOR,
        validators=[RegexValidator(
            '^([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|)$',
            'Color must be 3 or 6-digit hexecimal number, '
            'such as FF0000 for red.'), ])
    profile_text_color = models.CharField(
        max_length=7,
        blank=True,
        default=DEFAULT_PROFILE_TEXT_COLOR,
        validators=[RegexValidator('^([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|)$',
                                   'Color must be 3 or 6-digit hexecimal '
                                   'number, such as FF0000 for red.'), ])
    currency = models.ForeignKey(swapper.get_model_name(
        'accelerator', 'Currency'), blank=True,
        null=True, on_delete=models.CASCADE)

    location_national = models.CharField(
        max_length=100,
        blank=True,
        default='',
        help_text=('Please specify the country where your main office '
                   '(headquarters) is located'))
    location_regional = models.CharField(
        max_length=100,
        blank=True,
        default='',
        help_text=('Please specify the state, region or province where your '
                   'main office (headquarters) is located (if applicable).'))
    location_city = models.CharField(
        max_length=100,
        blank=True,
        default='',
        help_text=('Please specify the city where your main '
                   'office (headquarters) is located. (e.g. Boston)'))
    location_postcode = models.CharField(
        max_length=100,
        blank=True,
        default='',
        help_text=('Please specify the postal code for your main office '
                   '(headquarters). (ZIP code, Postcode, codigo postal, '
                   'etc.)'))
    date_founded = models.CharField(
        max_length=100,
        blank=True,
        help_text='Month and Year when your startup was founded.'
    )
    landing_page = models.CharField(max_length=255, null=True, blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_startup'
        abstract = True
        verbose_name_plural = 'Startups'
        ordering = ['organization__name']

    def __str__(self):
        return self.name or ""

    @property
    def name(self):
        return self._get_org_attr("name")

    @name.setter
    def name(self, value):
        self._set_org_attr("name", value)

    @property
    def website_url(self):
        return self._get_org_attr("website_url")

    @website_url.setter
    def website_url(self, website_url):
        self._set_org_attr("website_url", website_url)

    @property
    def twitter_handle(self):
        return self._get_org_attr("twitter_handle")

    @twitter_handle.setter
    def twitter_handle(self, twitter_handle):
        self._set_org_attr("twitter_handle", twitter_handle)

    @property
    def public_inquiry_email(self):
        return self._get_org_attr("public_inquiry_email")

    @public_inquiry_email.setter
    def public_inquiry_email(self, public_inquiry_email):
        self._set_org_attr("public_inquiry_email", public_inquiry_email)

    def _get_org_attr(self, attr):
        if self.organization:
            return getattr(self.organization, attr)
        else:
            logger.warning(STARTUP_NO_ORG_WARNING_MSG.format(self.pk))
            return None

    def _set_org_attr(self, attr, value):
        if self.organization:
            setattr(self.organization, attr, value)
            self.organization.save()
            return
        else:
            logger.warning(STARTUP_NO_ORG_WARNING_MSG.format(self.pk))
            return None

    @property
    def image_url(self):
        if self.high_resolution_logo:
            return self.high_resolution_logo.url
        return ""

    def program_startup_statuses(self):
        from accelerator.models.program_startup_status import (
            ProgramStartupStatus
        )
        return ProgramStartupStatus.objects.filter(
            startupstatus__startup=self)

    def _generate_formatted_startup_status(self, status):
        program = status.program
        formatted_status = DISPLAY_STARTUP_STATUS.format(
            status=status.startup_role.name,
            year=str(program.start_date.year),
            program_family_slug=program.program_family.url_slug.upper()
        )
        return formatted_status

    def _get_finalist_startup_statuses(self):
        roles_of_interest = (
            BaseStartupRole.FINALIST_STARTUP_ROLES +
            BaseStartupRole.WINNER_STARTUP_ROLES
        )
        statuses = self.program_startup_statuses().filter(
                startup_role__name__in=roles_of_interest
                    ).order_by("-created_at")
        return statuses

    @property
    def finalist_startup_statuses(self):
        statuses = self._get_finalist_startup_statuses()
        status_list = [
            self._generate_formatted_startup_status(status)
            for status in statuses]
        return status_list

    @property
    def latest_status_year(self):
        statuses = self._get_finalist_startup_statuses()
        if statuses:
            return statuses[0].program.start_date.year
        return 0

    def is_finalist(self, program=None):
        """if program is given, check whether this startup is a finalist
        in that program. Otherwise, check whether this startup is a finalist
        in any program"""
        if program is None:
            return self.program_startup_statuses().filter(
                startup_role__name=BaseStartupRole.FINALIST).exists()
        return self.program_startup_statuses().filter(
            startup_role__name=BaseStartupRole.FINALIST,
            program__exact=program
        ).exists()

    is_finalist.boolean = True

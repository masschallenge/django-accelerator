# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import logging

import swapper
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField

from accelerator_abstract.models.accelerator_model import AcceleratorModel

logger = logging.getLogger(__name__)

DEFAULT_PROFILE_BACKGROUND_COLOR = '217181'  # default dark blue

DEFAULT_PROFILE_TEXT_COLOR = 'FFFFFF'

STARTUP_COMMUNITIES = (
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
)
STARTUP_NO_ORG_WARNING_MSG = "Startup {} has no organization"


@python_2_unicode_compatible
class BaseStartup(AcceleratorModel):
    organization = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, 'Organization'), blank=True,
        null=True, related_name='startups')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_visible = models.BooleanField(
        default=True,
        help_text=('Startup Profiles will be published to external websites '
                   'through the the API.'))
    primary_industry = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Industry'),
        verbose_name='Primary Industry categorization',
        related_name='startups')
    additional_industries = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Industry'),
        verbose_name='Additional Industries',
        related_name='secondary_startups',
        db_table="{}_startup_related_industry".format(
            AcceleratorModel.Meta.app_label),
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
    linked_in_url = models.URLField(max_length=100, blank=True)
    facebook_url = models.URLField(max_length=100, blank=True)
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
    recommendation_tags = models.ManyToManyField(
        swapper.get_model_name('accelerator', 'RecommendationTag'),
        blank=True)
    currency = models.ForeignKey(swapper.get_model_name(
        'accelerator', 'Currency'), blank=True,
        null=True)

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
        db_table = '{}_startup'.format(AcceleratorModel.Meta.app_label)
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

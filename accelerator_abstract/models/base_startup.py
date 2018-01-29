# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField

from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

from accelerator_abstract.models.accelerator_model import AcceleratorModel
import swapper

DEFAULT_PROFILE_BACKGROUND_COLOR = '217181'  # default dark blue

DEFAULT_PROFILE_TEXT_COLOR = 'FFFFFF'

STARTUP_COMMUNITIES = (
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
)


@python_2_unicode_compatible
class BaseStartup(AcceleratorModel):
    organization = models.ForeignKey(swapper.get_model_name(
        'accelerator', 'Organization'), blank=True,
        null=True, related_name='startups')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='acc_startups')
    is_visible = models.BooleanField(
        default=True,
        help_text=('Startup Profiles will be published to external websites '
                   'through the the API.'))
    primary_industry = models.ForeignKey(
        swapper.get_model_name('accelerator', 'Industry'),
        verbose_name='Primary Industry categorization',
        related_name='startups')
    additional_industries = models.ManyToManyField(
        settings.MPTT_SWAPPABLE_INDUSTRY_MODEL_ADDITIONAL,
        verbose_name='Additional Industries',
        related_name='secondary_startups',
        db_table=settings.MPTT_SWAPPABLE_INDUSTRY_DB_TABLE_NAME,
        blank=True,
        help_text='You may select up to 5 related industries.',
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
            'The Startup Profile video is great way to show off your '
            'startup to the judges and the broader MassChallenge '
            'community (if you\'re not in stealth mode). Brevity is '
            'recommended and videos should not be longer than 1-3 '
            'minutes. Please submit YouTube or Vimeo URLs.')
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
        return self.organization.name

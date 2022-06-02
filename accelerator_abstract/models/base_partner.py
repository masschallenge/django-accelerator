from __future__ import unicode_literals

import swapper
from django.db import models
from sorl.thumbnail import ImageField

from embed_video.fields import EmbedVideoField

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BasePartner(AcceleratorModel):
    organization = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "Organization"), null=True, blank=True,
        on_delete=models.CASCADE)
    description = models.TextField(
        max_length=1000,
        blank=True,
        help_text='This is the generic description of the Partner, shared '
                  'across all Programs.')
    partner_logo = ImageField(
        upload_to='startup_pics',
        verbose_name="Partner Logo",
        blank=True)
    primary_industry = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Industry'),
        verbose_name='Primary Industry categorization', blank=True, null=True,
        related_name='partners', on_delete=models.CASCADE)
    additional_industries = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Industry'),
        verbose_name='Additional Industries',
        related_name='secondary_partners',
        db_table="accelerator_partner_related_industry",
        blank=True,
        null=True,
        help_text=(
            'You may select up to 5 related industries.'),)
    date_founded = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Month and Year when your partner was founded.')
    location_street_address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
        help_text=('Please specify the street address for your main office '
                   '(headquarters).'))
    location_city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
        help_text=('Please specify the city where your main '
                   'office (headquarters) is located. (e.g. Boston)'))
    location_regional = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
        help_text=('Please specify the state, region or province where your '
                   'main office (headquarters) is located (if applicable).'))
    location_national = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
        help_text=('Please specify the country where your main office '
                   '(headquarters) is located'))
    short_pitch = models.TextField(
        max_length=140,
        blank=True,
        null=True,
        help_text='Your enterprise in 140 characters or less.')
    full_elevator_pitch = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        help_text='Your enterprise in 140 characters or less.')
    video_elevator_pitch_url = EmbedVideoField(
        max_length=100,
        blank=True, null=True,
        help_text=(
            'Upload your 1-3 minute video pitch to Vimeo or Youtube. '
            'Paste the shared link here.'))
    public_inquiry_email = models.URLField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Public Inquiry email")
    website_url = models.URLField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Website URL")
    twitter_handle = models.URLField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Twitter profile URL")
    linked_in_url = models.URLField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="LinkedIn profile URL")
    facebook_url = models.URLField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Facebook profile URL")
    is_visible = models.BooleanField(
        default=True,
        blank=True,
        help_text=('Partner Profiles will be published to external websites '
                   'through the the API.'))

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_partner'
        abstract = True
        verbose_name_plural = 'Partners'
        ordering = ['organization__name', ]

    def __str__(self):
        return self.organization.name

    @property
    def name(self):
        return self.organization.name

    @name.setter
    def name(self, name):
        self.organization.name = name
        self.organization.save()

    @property
    def website_url(self):
        return self.organization.website_url

    @website_url.setter
    def website_url(self, website_url):
        self.organization.website_url = website_url
        self.organization.save()

    @property
    def twitter_handle(self):
        return self.organization.twitter_handle

    @twitter_handle.setter
    def twitter_handle(self, twitter_handle):
        self.organization.twitter_handle = twitter_handle
        self.organization.save()

    @property
    def public_inquiry_email(self):
        return self.organization.public_inquiry_email

    @public_inquiry_email.setter
    def public_inquiry_email(self, public_inquiry_email):
        self.organization.public_inquiry_email = public_inquiry_email
        self.organization.save()

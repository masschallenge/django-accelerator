# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from sorl.thumbnail import ImageField

from accelerator_abstract.models.accelerator_model import AcceleratorModel

GENDER_MALE_CHOICE = ('m', 'Male')
GENDER_FEMALE_CHOICE = ('f', 'Female')
GENDER_OTHER_CHOICE = ('o', 'Other')
GENDER_PREFER_NOT_TO_STATE_CHOICE = ('p', 'Prefer Not To State')
GENDER_UNKNOWN_CHOICE = ('', 'Unknown')

GENDER_CHOICES = (
    GENDER_FEMALE_CHOICE,
    GENDER_MALE_CHOICE,
    GENDER_PREFER_NOT_TO_STATE_CHOICE,
    GENDER_OTHER_CHOICE,
    GENDER_UNKNOWN_CHOICE,
)

UI_GENDER_CHOICES = (
    GENDER_FEMALE_CHOICE,
    GENDER_MALE_CHOICE,
    GENDER_PREFER_NOT_TO_STATE_CHOICE,
    GENDER_OTHER_CHOICE,
)


@python_2_unicode_compatible
class BaseCoreProfile(AcceleratorModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='')
    phone = models.CharField(
        verbose_name="Phone",
        max_length=20,
        validators=[RegexValidator(
            regex='^[0-9x.+() -]+$',
            message='Digits and +()-.x only')],
        blank=True)
    linked_in_url = models.URLField(
        verbose_name="LinkedIn",
        blank=True)
    facebook_url = models.URLField(
        verbose_name="Facebook",
        blank=True)
    twitter_handle = models.CharField(
        verbose_name="Twitter",
        max_length=40,
        blank=True)
    personal_website_url = models.URLField(
        verbose_name="Website",
        max_length=255,
        blank=True)
    landing_page = models.CharField(
        verbose_name="Current landing page within the site",
        validators=[RegexValidator(
            "^[^:]*$",
            "Must be a page within the site"), ],
        max_length=200,
        blank=True)
    image = ImageField(
        upload_to='profile_pics',
        verbose_name="Profile Picture",
        help_text="Suggested size: <400px on the short side",
        blank=True)
    drupal_id = models.IntegerField(blank=True, null=True)
    drupal_creation_date = models.DateTimeField(blank=True, null=True)
    drupal_last_login = models.DateTimeField(blank=True, null=True)
    interest_categories = models.ManyToManyField(
        to=swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                  'InterestCategory'),
        blank=True)
    users_last_activity = models.DateTimeField(blank=True, null=True)
    current_program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'Program'),
        blank=True,
        null=True,
    )
    program_families = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'ProgramFamily'),
        help_text="Which of our Program Families would you like to be "
                  "involved with?",
        related_name="interested_%(class)s",
        blank=True
    )

    user_type = None
    default_page = "member_homepage"
    recommendation_tags = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'RecommendationTag'),
        blank=True)
    newsletter_sender = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_coreprofile'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        identifier = self.full_name()
        ptype = ''
        if self.user_type is not None:
            ptype = ("%s " % self.user_type).title()
        return "%sProfile for %s" % (ptype, identifier)

    def full_name(self):
        return self.user.full_name()

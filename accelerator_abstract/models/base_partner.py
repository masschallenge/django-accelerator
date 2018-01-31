# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from sorl.thumbnail import ImageField

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BasePartner(AcceleratorModel):
    organization = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "Organization"), null=True, blank=True)
    description = models.TextField(
        max_length=1000,
        blank=True,
        help_text='This is the generic description of the Partner, shared '
                  'across all Programs.')
    partner_logo = ImageField(
        upload_to='startup_pics',
        verbose_name="Partner Logo",
        blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_partner'.format(
            AcceleratorModel.Meta.app_label)
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

    def user_is_team_member(self, user_id):
        if self.partnerteammember_set.filter(team_member__pk=user_id).exists():
            return True
        return False
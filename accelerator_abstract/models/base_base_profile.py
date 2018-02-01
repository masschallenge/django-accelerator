# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.managers.profile_manager import ProfileManager
from accelerator_abstract.models.accelerator_model import AcceleratorModel

ENTREPRENEUR_USER_TYPE = 'ENTREPRENEUR'
EXPERT_USER_TYPE = 'EXPERT'
MEMBER_USER_TYPE = 'MEMBER'

USER_TYPES = ((EXPERT_USER_TYPE, 'Expert'),
              (ENTREPRENEUR_USER_TYPE, 'Entrepreneur'),
              (MEMBER_USER_TYPE, 'Member'))

TWITTER_HANDLE_MAX_LENGTH = 16
PHONE_MAX_LENGTH = 20


@python_2_unicode_compatible
class BaseBaseProfile(AcceleratorModel):
    """pivot class that returns an appropriate profile based on user_type

    see: ProfileManager
    """
    objects = ProfileManager()
    manager = models.Manager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="baseprofile")
    user_type = models.CharField(max_length=16, choices=USER_TYPES)
    privacy_policy_accepted = models.BooleanField(
        default=False,
        blank=False,
        null=False)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_baseprofile'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        fn = self.user.first_name
        ln = self.user.last_name
        if fn and ln:
            identifier = "%s %s" % (fn, ln)
        else:
            identifier = self.user.email
        return "Base Profile for %s" % identifier

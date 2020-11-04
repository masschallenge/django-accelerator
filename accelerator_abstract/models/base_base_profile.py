# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

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

    see: accelerator.models.ProfileManager
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="baseprofile",
                                on_delete=models.CASCADE)
    user_type = models.CharField(max_length=16, choices=USER_TYPES)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_baseprofile'
        abstract = True

    def __str__(self):
        identifier = self.user.full_name()
        return "Base Profile for %s" % identifier

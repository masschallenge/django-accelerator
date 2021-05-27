# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


import swapper
from django.db import models

from accelerator_abstract.models.base_core_profile import BaseCoreProfile



class BaseExpertProfile(BaseCoreProfile):
    user_type = 'expert'
    default_page = "expert_homepage"

    class Meta(BaseCoreProfile.Meta):
        db_table = 'accelerator_expertprofile'
        abstract = True
        permissions = (
            ('change_password', 'Can change users passwords directly'),
        )

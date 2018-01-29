# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BaseMemberProfile
from accelerator_abstract.models.accelerator_model import AcceleratorModel


class MemberProfile(BaseMemberProfile):
    class Meta(BaseMemberProfile.Meta):
        swappable = swapper.swappable_setting(
            BaseMemberProfile.Meta.app_label, "MemberProfile")

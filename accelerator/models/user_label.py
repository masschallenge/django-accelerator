# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
from django.conf import settings

from accelerator_abstract.models.base_user_label import BaseUserLabel


class UserLabel(BaseUserLabel):
    class Meta(BaseUserLabel.Meta):
        swappable = swapper.swappable_setting(
            BaseUserLabel.Meta.app_label, "UserLabel")

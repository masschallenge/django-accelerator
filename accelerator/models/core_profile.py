# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import swapper

from sorl.thumbnail import ImageField

from accelerator_abstract.models.base_core_profile import BaseCoreProfile
from accelerator_abstract.utils import url_validator


class CoreProfile(BaseCoreProfile):
    class Meta(BaseCoreProfile.Meta):
        swappable = swapper.swappable_setting(
            BaseCoreProfile.Meta.app_label, "CoreProfile")

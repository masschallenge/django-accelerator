# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models

from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BaseApplicationType
from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class ApplicationType(BaseApplicationType):
    class Meta(AcceleratorModel.Meta):
        swappable = swapper.swappable_setting(
            BaseApplicationType.Meta.app_label, "ApplicationType")

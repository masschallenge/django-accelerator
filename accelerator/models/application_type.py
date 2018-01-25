# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper

from accelerator_abstract.models import BaseApplicationType
from accelerator_abstract.models.accelerator_model import AcceleratorModel


class ApplicationType(BaseApplicationType):
    class Meta(AcceleratorModel.Meta):
        swappable = swapper.swappable_setting(
            BaseApplicationType.Meta.app_label, "ApplicationType")

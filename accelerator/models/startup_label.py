# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BaseStartupLabel
from accelerator_abstract.models.label_model import LabelModel


@python_2_unicode_compatible
class StartupLabel(BaseStartupLabel):
    class Meta(LabelModel.Meta):
        swappable = swapper.swappable_setting(BaseStartupLabel.Meta.app_label,
                                              "StartupLabel")

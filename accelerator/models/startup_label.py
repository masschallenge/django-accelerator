# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BaseStartupLabel
from accelerator_abstract.models.label_model import LabelModel


class StartupLabel(BaseStartupLabel):
    class Meta(LabelModel.Meta):
        swappable = swapper.swappable_setting(BaseStartupLabel.Meta.app_label,
                                              "StartupLabel")

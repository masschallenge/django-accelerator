# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseStartupLabel
from accelerator_abstract.models.label_model import LabelModel


class StartupLabel(BaseStartupLabel):
    class Meta(LabelModel.Meta):
        swappable = False

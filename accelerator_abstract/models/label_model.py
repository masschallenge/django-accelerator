# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from .accelerator_model import AcceleratorModel


class LabelModel(AcceleratorModel):
    LABEL_LENGTH = 255
    pass

    class Meta(AcceleratorModel.Meta):
        abstract = True

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseApplicationQuestion
from accelerator_abstract.models.accelerator_model import AcceleratorModel


class ApplicationQuestion(BaseApplicationQuestion):
    class Meta(AcceleratorModel.Meta):
        swappable = False

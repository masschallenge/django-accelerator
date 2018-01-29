# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models

from accelerator_abstract.models.base_model_change import BaseModelChange


class ModelChange(BaseModelChange):
    class Meta(BaseModelChange.Meta):
        swappable = swapper.swappable_setting(
            BaseModelChange.Meta.app_label, "ModelChange")

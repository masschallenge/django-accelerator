# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_model_change import BaseModelChange


class ModelChange(BaseModelChange):
    class Meta(BaseModelChange.Meta):
        swappable = swapper.swappable_setting(
            BaseModelChange.Meta.app_label, "ModelChange")

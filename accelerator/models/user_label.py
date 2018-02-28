# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_user_label import BaseUserLabel


class UserLabel(BaseUserLabel):
    class Meta(BaseUserLabel.Meta):
        swappable = swapper.swappable_setting(
            BaseUserLabel.Meta.app_label, "UserLabel")

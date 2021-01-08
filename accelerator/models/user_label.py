# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_user_label import BaseUserLabel


class UserLabel(BaseUserLabel):
    class Meta(BaseUserLabel.Meta):
        swappable = False

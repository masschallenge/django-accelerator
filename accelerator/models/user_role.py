# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_user_role import BaseUserRole


class UserRole(BaseUserRole):
    class Meta(BaseUserRole.Meta):
        swappable = False

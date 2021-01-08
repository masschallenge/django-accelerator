# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_user_role_menu import BaseUserRoleMenu


class UserRoleMenu(BaseUserRoleMenu):
    class Meta(BaseUserRoleMenu.Meta):
        swappable = False

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_user_role_menu import BaseUserRoleMenu


class UserRoleMenu(BaseUserRoleMenu):
    class Meta(BaseUserRoleMenu.Meta):
        swappable = swapper.swappable_setting(BaseUserRoleMenu.Meta.app_label,
                                              'UserRoleMenu')

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_user_role import BaseUserRole


class UserRole(BaseUserRole):
    class Meta(BaseUserRole.Meta):
        swappable = swapper.swappable_setting(
            BaseUserRole.Meta.app_label, "UserRole")

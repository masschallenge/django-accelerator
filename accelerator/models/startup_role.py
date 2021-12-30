from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_startup_role import BaseStartupRole


class StartupRole(BaseStartupRole):
    class Meta(BaseStartupRole.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupRole.Meta.app_label, "StartupRole")

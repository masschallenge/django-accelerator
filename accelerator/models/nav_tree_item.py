from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_nav_tree_item import BaseNavTreeItem


class NavTreeItem(BaseNavTreeItem):
    class Meta(BaseNavTreeItem.Meta):
        swappable = swapper.swappable_setting(BaseNavTreeItem.Meta.app_label,
                                              "NavTreeItem")

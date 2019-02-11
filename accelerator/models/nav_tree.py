from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_nav_tree import BaseNavTree


class NavTree(BaseNavTree):
    class Meta(BaseNavTree.Meta):
        swappable = swapper.swappable_setting(BaseNavTree.Meta.app_label,
                                              "NavTree")

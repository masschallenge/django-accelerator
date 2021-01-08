from __future__ import unicode_literals


from accelerator_abstract.models.base_nav_tree_item import BaseNavTreeItem


class NavTreeItem(BaseNavTreeItem):
    class Meta(BaseNavTreeItem.Meta):
        swappable = False

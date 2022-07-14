import swapper

from accelerator.models.nav_tree import NavTree
from accelerator_abstract.models.base_nav_tree_item import BaseNavTreeItem

SUB_NAV_ALIAS_FORMAT = '{}_subnav'


class NavTreeItem(BaseNavTreeItem):
    class Meta(BaseNavTreeItem.Meta):
        swappable = swapper.swappable_setting(BaseNavTreeItem.Meta.app_label,
                                              "NavTreeItem")

    def sub_nav_tree(self):
        return NavTree.objects.filter(
            alias=SUB_NAV_ALIAS_FORMAT.format(self.alias)
        ).first()

    def sub_nav_tree_items(self):
        sub_nav_tree = self.sub_nav_tree()
        if sub_nav_tree:
            return NavTreeItem.objects.filter(tree=sub_nav_tree)
        return []

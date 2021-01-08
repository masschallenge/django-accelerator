from __future__ import unicode_literals


from accelerator_abstract.models.base_nav_tree import BaseNavTree


class NavTree(BaseNavTree):
    class Meta(BaseNavTree.Meta):
        swappable = False

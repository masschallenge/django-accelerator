from __future__ import unicode_literals

from sitetree.models import TreeBase

from accelerator_abstract.models.accelerator_model import AcceleratorModel

MC_SIDE_NAV_TREE_ALIAS = 'mc_side_nav_tree'


class BaseNavTree(TreeBase, AcceleratorModel):
    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_navtree'
        verbose_name_plural = "NavTrees"
        abstract = True

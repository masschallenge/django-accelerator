from __future__ import unicode_literals

from sitetree.models import TreeBase

from accelerator_abstract.models.accelerator_model import AcceleratorModel

MC_SIDE_NAV_TREE_ALIAS = 'mc_side_nav_tree'

class BaseNavTree(TreeBase, AcceleratorModel):
    class Meta(AcceleratorModel.Meta):
        db_table = '{}_navtree'.format(AcceleratorModel.Meta.app_label)
        verbose_name_plural = "NavTrees"
        abstract = True

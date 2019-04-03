# MIT License
# Copyright (c) 2018 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from fluent_pages.models import UrlNode

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseNodeSideNavAssociation(AcceleratorModel):
    node = models.ForeignKey(UrlNode)
    side_nav = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "NavTree"))
    sub_nav_item = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "NavTreeItem"), null=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_nodesidenavassociation'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Side Nav Association"
        verbose_name_plural = "Fluent page link will show up on"

    def __str__(self):
        tmpl = "%s will show up on the %s sub navigation"
        return tmpl % (self.node.title, self.side_nav.title)

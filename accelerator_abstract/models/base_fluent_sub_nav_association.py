# MIT License
# Copyright (c) 2019 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from fluent_pages.models import UrlNode

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseNodeSubNavAssociation(AcceleratorModel):
    node = models.ForeignKey(UrlNode, on_delete=models.CASCADE)
    sub_nav = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "NavTree"),
        help_text=(
            'This is the sub navigation tree '
            'that this page is tied to'
        ),
        on_delete=models.CASCADE
    )
    sub_nav_item = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "NavTreeItem"),
        null=True,
        help_text=(
            'This is the sub navigation '
            'item that this page is tied to'),
        on_delete=models.CASCADE
    )

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_nodesubnavassociation'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Node Sub Navigation Association"
        verbose_name_plural = "Node Sub Navigation Associations"

    def __str__(self):
        tmpl = "%s will show up on the %s sub navigation"
        return tmpl % (self.node.title, self.sub_nav.title)

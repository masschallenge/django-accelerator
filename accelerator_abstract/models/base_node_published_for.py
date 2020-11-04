# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from fluent_pages.models import UrlNode

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseNodePublishedFor(AcceleratorModel):
    node = models.ForeignKey(UrlNode, on_delete=models.CASCADE)
    published_for = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "ProgramRole"),
        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_nodepublishedfor'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "Node is Published For"
        verbose_name_plural = "Node is Published For"

    def __str__(self):
        tmpl = "%s is available to %s"
        return tmpl % (self.node.title, self.published_for.name)

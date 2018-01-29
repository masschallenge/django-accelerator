# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
from fluent_pages.models import UrlNode

from accelerator_abstract.models.base_node_published_for import (
    BaseNodePublishedFor
)


class NodePublishedFor(BaseNodePublishedFor):
    class Meta(BaseNodePublishedFor.Meta):
        swappable = swapper.swappable_setting(
            BaseNodePublishedFor.Meta.app_label, "NodePublishedFor")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_node_published_for import (
    BaseNodePublishedFor
)


class NodePublishedFor(BaseNodePublishedFor):
    class Meta(BaseNodePublishedFor.Meta):
        swappable = False

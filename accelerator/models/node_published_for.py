# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_node_published_for import (
    BaseNodePublishedFor
)


class NodePublishedFor(BaseNodePublishedFor):
    class Meta(BaseNodePublishedFor.Meta):
        swappable = swapper.swappable_setting(
            BaseNodePublishedFor.Meta.app_label, "NodePublishedFor")

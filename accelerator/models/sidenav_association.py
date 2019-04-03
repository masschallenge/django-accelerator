# MIT License
# Copyright (c) 2018 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseNodeSideNavAssociation


class NodeSideNavAssociation(BaseNodeSideNavAssociation):
    class Meta(BaseNodeSideNavAssociation.Meta):
        swappable = swapper.swappable_setting(
            BaseNodeSideNavAssociation.Meta.app_label,
            "NodeSideNavAssociation")

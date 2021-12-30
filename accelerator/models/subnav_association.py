from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseNodeSubNavAssociation


class NodeSubNavAssociation(BaseNodeSubNavAssociation):
    class Meta(BaseNodeSubNavAssociation.Meta):
        swappable = swapper.swappable_setting(
            BaseNodeSubNavAssociation.Meta.app_label,
            "NodeSubNavAssociation")

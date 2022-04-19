from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseIndustryCluster


class IndustryCluster(BaseIndustryCluster):
    class Meta(BaseIndustryCluster.Meta):
        swappable = swapper.swappable_setting(
            BaseIndustryCluster.Meta.app_label,
            "IndustryCluster")

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseExpertInterest


class ExpertInterest(BaseExpertInterest):
    class Meta(BaseExpertInterest.Meta):
        swappable = swapper.swappable_setting(
            BaseExpertInterest.Meta.app_label, "ExpertInterest")

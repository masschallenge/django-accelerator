from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseInterestCategory


class InterestCategory(BaseInterestCategory):
    class Meta(BaseInterestCategory.Meta):
        swappable = swapper.swappable_setting(
            BaseInterestCategory.Meta.app_label, "InterestCategory")

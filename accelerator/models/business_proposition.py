from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseBusinessProposition


class BusinessProposition(BaseBusinessProposition):
    class Meta(BaseBusinessProposition.Meta):
        swappable = swapper.swappable_setting(
            BaseBusinessProposition.Meta.app_label, "BusinessProposition")

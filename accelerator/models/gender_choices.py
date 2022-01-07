from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseGenderChoices


class GenderChoices(BaseGenderChoices):
    class Meta(BaseGenderChoices.Meta):
        swappable = swapper.swappable_setting(
            BaseGenderChoices.Meta.app_label, "GenderChoices")

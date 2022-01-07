from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseJudgeAvailability


class JudgeAvailability(BaseJudgeAvailability):
    class Meta(BaseJudgeAvailability.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgeAvailability.Meta.app_label, "JudgeAvailability")

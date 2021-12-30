from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseJudgingForm


class JudgingForm(BaseJudgingForm):
    class Meta(BaseJudgingForm.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgingForm.Meta.app_label, "JudgingForm")

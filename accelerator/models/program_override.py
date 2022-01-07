from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseProgramOverride


class ProgramOverride(BaseProgramOverride):
    class Meta(BaseProgramOverride.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramOverride.Meta.app_label, "ProgramOverride")

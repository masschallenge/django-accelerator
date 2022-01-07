from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseProgramFamily


class ProgramFamily(BaseProgramFamily):
    class Meta(BaseProgramFamily.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramFamily.Meta.app_label, "ProgramFamily")

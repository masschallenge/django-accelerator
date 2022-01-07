from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseProgramRole


class ProgramRole(BaseProgramRole):
    class Meta(BaseProgramRole.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramRole.Meta.app_label, "ProgramRole")

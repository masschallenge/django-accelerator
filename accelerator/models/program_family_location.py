from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_program_family_location import (
    BaseProgramFamilyLocation
)


class ProgramFamilyLocation(BaseProgramFamilyLocation):
    class Meta(BaseProgramFamilyLocation.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramFamilyLocation.Meta.app_label, "ProgramFamilyLocation")

from __future__ import unicode_literals


from accelerator_abstract.models.base_program_family_location import (
    BaseProgramFamilyLocation
)


class ProgramFamilyLocation(BaseProgramFamilyLocation):
    class Meta(BaseProgramFamilyLocation.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_program_role_grant import (
    BaseProgramRoleGrant
)


class ProgramRoleGrant(BaseProgramRoleGrant):
    class Meta(BaseProgramRoleGrant.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramRoleGrant.Meta.app_label, "ProgramRoleGrant")

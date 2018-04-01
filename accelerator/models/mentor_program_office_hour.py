# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_mentor_program_office_hour import (
    BaseMentorProgramOfficeHour,
)


class MentorProgramOfficeHour(BaseMentorProgramOfficeHour):
    class Meta(BaseMentorProgramOfficeHour.Meta):
        swappable = swapper.swappable_setting(
            BaseMentorProgramOfficeHour.Meta.app_label,
            "MentorProgramOfficeHour")

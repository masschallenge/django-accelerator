# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_startup_mentor_relationship import (
    BaseStartupMentorRelationship
)


class StartupMentorRelationship(BaseStartupMentorRelationship):
    class Meta(BaseStartupMentorRelationship.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupMentorRelationship.Meta.app_label,
            "StartupMentorRelationship")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_startup_mentor_tracking_record import (
    BaseStartupMentorTrackingRecord
)


class StartupMentorTrackingRecord(BaseStartupMentorTrackingRecord):
    class Meta(BaseStartupMentorTrackingRecord.Meta):
        swappable = swapper.swappable_setting(
            BaseStartupMentorTrackingRecord.Meta.app_label,
            "StartupMentorTrackingRecord")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseMemberProfile


class MemberProfile(BaseMemberProfile):
    class Meta(BaseMemberProfile.Meta):
        swappable = swapper.swappable_setting(
            BaseMemberProfile.Meta.app_label, "MemberProfile")

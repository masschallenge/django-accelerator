# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator.tests.factories.core_profile_factory import CoreProfileFactory

from accelerator.models import MemberProfile


class MemberProfileFactory(CoreProfileFactory):
    class Meta:
        model = MemberProfile

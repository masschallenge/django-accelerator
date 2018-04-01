# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import RelatedFactory

from accelerator.tests.factories.base_profile_factory import BaseProfileFactory
from accelerator.tests.factories.member_profile_factory import (
    MemberProfileFactory
)
from simpleuser.tests.factories.user_factory import UserFactory
from accelerator_abstract.models.base_base_profile import MEMBER_USER_TYPE


class MemberFactory(UserFactory):
    baseprofile = RelatedFactory(BaseProfileFactory, "user",
                                 user_type=MEMBER_USER_TYPE)
    profile = RelatedFactory(MemberProfileFactory, "user")

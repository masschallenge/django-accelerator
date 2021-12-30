from __future__ import unicode_literals

from factory import (
    RelatedFactory,
)

from accelerator.tests.factories.base_profile_factory import BaseProfileFactory
from accelerator.tests.factories.expert_profile_factory import (
    ExpertProfileFactory
)
from simpleuser.tests.factories.user_factory import UserFactory


class ExpertFactory(UserFactory):
    baseprofile = RelatedFactory(BaseProfileFactory, "user",
                                 user_type="EXPERT")
    profile = RelatedFactory(ExpertProfileFactory, "user")

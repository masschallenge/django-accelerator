from factory import (
    RelatedFactory,
)

from accelerator.tests.factories.base_profile_factory import BaseProfileFactory
from accelerator.tests.factories.entrepreneur_profile_factory import EntrepreneurProfileFactory
from accelerator.tests.factories.user_factory import UserFactory


class EntrepreneurFactory(UserFactory):
    baseprofile = RelatedFactory(BaseProfileFactory, "user")
    profile = RelatedFactory(EntrepreneurProfileFactory, "user")

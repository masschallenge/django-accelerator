import swapper

from datetime import (
    datetime,
    timedelta,
)
from factory import SubFactory
from factory.django import DjangoModelFactory
from simpleuser.tests.factories.user_factory import UserFactory
from .deferrable_modal_factory import DeferrableModalFactory

UserDeferrableModal = swapper.load_model('accelerator', 'UserDeferrableModal')


class UserDeferrableModalFactory(DjangoModelFactory):
    class Meta:
        model = UserDeferrableModal

    user = SubFactory(UserFactory)
    deferrable_modal = SubFactory(DeferrableModalFactory)
    is_deferred = False
    deferred_to = datetime.now() + timedelta(days=1)



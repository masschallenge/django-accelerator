import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.user_factory import UserFactory

BaseProfile = swapper.load_model(AcceleratorConfig.name, 'BaseProfile')


class BaseProfileFactory(DjangoModelFactory):
    class Meta:
        model = BaseProfile

    user = SubFactory(UserFactory)
    user_type = "ENTREPRENEUR"
    privacy_policy_accepted = True

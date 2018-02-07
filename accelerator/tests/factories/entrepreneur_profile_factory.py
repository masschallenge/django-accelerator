import swapper

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.core_profile_factory import CoreProfileFactory

EntrepreneurProfile = swapper.load_model(AcceleratorConfig.name,
                                         'EntrepreneurProfile')


class EntrepreneurProfileFactory(CoreProfileFactory):
    privacy_policy_accepted = True

    class Meta:
        model = EntrepreneurProfile

    bio = "I was born at a very young age..."

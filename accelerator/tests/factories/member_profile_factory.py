import swapper

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.core_profile_factory import CoreProfileFactory

MemberProfile = swapper.load_model(AcceleratorConfig.name, 'MemberProfile')


class MemberProfileFactory(CoreProfileFactory):
    class Meta:
        model = MemberProfile

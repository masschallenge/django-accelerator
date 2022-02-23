from accelerator.models.core_profile import CoreProfile
from accelerator.tests.factories import CoreProfileFactory


class CoreProfileModelFactory(CoreProfileFactory):
    class Meta:
        model = CoreProfile

from __future__ import unicode_literals

import swapper

from accelerator.tests.factories.core_profile_factory import CoreProfileFactory

MemberProfile = swapper.load_model('accelerator', 'MemberProfile')


class MemberProfileFactory(CoreProfileFactory):
    class Meta:
        model = MemberProfile

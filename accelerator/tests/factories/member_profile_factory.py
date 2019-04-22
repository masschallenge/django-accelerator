# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.core_profile_factory import CoreProfileFactory

MemberProfile = swapper.load_model(AcceleratorConfig.name, 'MemberProfile')


class MemberProfileFactory(CoreProfileFactory):
    class Meta:
        model = MemberProfile

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        profile = model_class.objects.filter(user=kwargs['user'])
        if profile:
            profile.delete()
        manager = cls._get_manager(model_class)
        return manager.create(*args, **kwargs)

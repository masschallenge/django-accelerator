# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator.tests.factories.core_profile_factory import CoreProfileFactory

EntrepreneurProfile = swapper.load_model('accelerator', 'EntrepreneurProfile')


class EntrepreneurProfileFactory(CoreProfileFactory):
    class Meta:
        model = EntrepreneurProfile

    bio = "I was born at a very young age..."

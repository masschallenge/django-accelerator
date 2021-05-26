# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from polymorphic.models import PolymorphicModel

from accelerator_abstract.models.base_core_profile import BaseCoreProfile


class CoreProfile(BaseCoreProfile, PolymorphicModel):
    class Meta(BaseCoreProfile.Meta):
        pass

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_core_profile import BaseCoreProfile


class CoreProfile(BaseCoreProfile):
    class Meta(BaseCoreProfile.Meta):
        swappable = False
        abstract = True

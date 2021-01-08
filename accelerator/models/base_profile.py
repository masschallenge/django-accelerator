# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from accelerator.managers.profile_manager import ProfileManager
from accelerator_abstract.models.base_base_profile import BaseBaseProfile


class BaseProfile(BaseBaseProfile):
    objects = ProfileManager()
    manager = models.Manager()

    class Meta(BaseBaseProfile.Meta):
        swappable = False

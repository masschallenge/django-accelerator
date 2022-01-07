from __future__ import unicode_literals

import swapper
from django.db import models
from accelerator.managers.profile_manager import ProfileManager
from accelerator_abstract.models.base_base_profile import BaseBaseProfile


class BaseProfile(BaseBaseProfile):
    objects = ProfileManager()
    manager = models.Manager()

    class Meta(BaseBaseProfile.Meta):
        swappable = swapper.swappable_setting(
            BaseBaseProfile.Meta.app_label, "BaseProfile")

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper
from accelerator_abstract.models import BaseStartup
from django.conf import settings


class Startup(BaseStartup):
    class Meta(BaseStartup.Meta):
        swappable = swapper.swappable_setting(BaseStartup.Meta.app_label,
                                              'Startup')

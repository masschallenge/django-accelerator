# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseStartup


class Startup(BaseStartup):
    class Meta(BaseStartup.Meta):
        swappable = False

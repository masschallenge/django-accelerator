# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_startup_status import BaseStartupStatus


class StartupStatus(BaseStartupStatus):
    class Meta(BaseStartupStatus.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_startup_attribute import (
    BaseStartupAttribute
)


class StartupAttribute(BaseStartupAttribute):
    class Meta(BaseStartupAttribute.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_named_group import BaseNamedGroup


class NamedGroup(BaseNamedGroup):
    class Meta(BaseNamedGroup.Meta):
        swappable = False

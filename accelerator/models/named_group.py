# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.base_named_group import BaseNamedGroup


@python_2_unicode_compatible
class NamedGroup(BaseNamedGroup):
    class Meta(BaseNamedGroup.Meta):
        swappable = swapper.swappable_setting(BaseNamedGroup.Meta.app_label,
                                              "NamedGroup")

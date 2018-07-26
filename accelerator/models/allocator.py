# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_allocator import BaseAllocator


class Allocator(BaseAllocator):
    class Meta(BaseAllocator.Meta):
        swappable = swapper.swappable_setting(BaseAllocator.Meta.app_label,
                                              "Allocator")

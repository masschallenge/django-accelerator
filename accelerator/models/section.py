# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_section import BaseSection


class Section(BaseSection):
    class Meta(BaseSection.Meta):
        swappable = swapper.swappable_setting(
            BaseSection.Meta.app_label, "Section")

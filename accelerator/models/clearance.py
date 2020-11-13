# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_clearance import BaseClearance


class Clearance(BaseClearance):
    class Meta(BaseClearance.Meta):
        swappable = swapper.swappable_setting(
            BaseClearance.Meta.app_label, "Clearance")

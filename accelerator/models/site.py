# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_site import BaseSite


class Site(BaseSite):
    class Meta(BaseSite.Meta):
        swappable = swapper.swappable_setting(
            BaseSite.Meta.app_label, "Site")

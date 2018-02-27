# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_site_program_authorization import (
    BaseSiteProgramAuthorization
)


class SiteProgramAuthorization(BaseSiteProgramAuthorization):
    class Meta(BaseSiteProgramAuthorization.Meta):
        swappable = swapper.swappable_setting(
            BaseSiteProgramAuthorization.Meta.app_label,
            "SiteProgramAuthorization")

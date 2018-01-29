# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseEntrepreneurProfile


class EntrepreneurProfile(BaseEntrepreneurProfile):
    class Meta(BaseEntrepreneurProfile.Meta):
        swappable = swapper.swappable_setting(
            BaseEntrepreneurProfile.Meta.app_label, "EntrepreneurProfile")

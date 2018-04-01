# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseNewsletter


class Newsletter(BaseNewsletter):
    class Meta(BaseNewsletter.Meta):
        swappable = swapper.swappable_setting(
            BaseNewsletter.Meta.app_label, "Newsletter")

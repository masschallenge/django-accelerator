# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseObserver


class Observer(BaseObserver):
    class Meta(BaseObserver.Meta):
        swappable = swapper.swappable_setting(
            BaseObserver.Meta.app_label, "Observer")

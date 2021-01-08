# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseObserver


class Observer(BaseObserver):
    class Meta(BaseObserver.Meta):
        swappable = False

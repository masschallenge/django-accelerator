# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_application import BaseApplication


class Application(BaseApplication):
    class Meta(BaseApplication.Meta):
        swappable = False

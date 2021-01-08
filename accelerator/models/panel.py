# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_panel import BasePanel


class Panel(BasePanel):
    class Meta(BasePanel.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_site import BaseSite


class Site(BaseSite):
    class Meta(BaseSite.Meta):
        swappable = False

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseExpertProfile


class ExpertProfile(BaseExpertProfile):
    class Meta(BaseExpertProfile.Meta):
        swappable = False

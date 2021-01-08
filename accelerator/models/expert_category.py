# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseExpertCategory


class ExpertCategory(BaseExpertCategory):
    class Meta(BaseExpertCategory.Meta):
        swappable = False

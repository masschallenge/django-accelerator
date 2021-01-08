# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseInterestCategory


class InterestCategory(BaseInterestCategory):
    class Meta(BaseInterestCategory.Meta):
        swappable = False

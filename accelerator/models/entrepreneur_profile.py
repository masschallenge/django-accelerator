# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseEntrepreneurProfile


class EntrepreneurProfile(BaseEntrepreneurProfile):
    class Meta(BaseEntrepreneurProfile.Meta):
        swappable = False

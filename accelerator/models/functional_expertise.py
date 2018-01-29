# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from accelerator_abstract.models import BaseFunctionalExpertise


class FunctionalExpertise(BaseFunctionalExpertise):
    class Meta(BaseFunctionalExpertise.Meta):
        swappable = 'MPTT_SWAPPABLE_FUNCTIONALEXPERTISE_MODEL'

# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_bucket_state import BaseBucketState


class BucketState(BaseBucketState):
    class Meta(BaseBucketState.Meta):
        swappable = False

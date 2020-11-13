# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


from django.test import TestCase

from .factories import (
    BucketStateFactory,
)


class TestBucketState(TestCase):

    def test_str(self):
        bucket_state = BucketStateFactory()
        assert bucket_state.name in str(bucket_state)

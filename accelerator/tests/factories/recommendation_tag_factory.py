# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

RecommendationTag = swapper.load_model('accelerator', 'RecommendationTag')


class RecommendationTagFactory(DjangoModelFactory):
    class Meta:
        model = RecommendationTag

    text = Sequence(lambda n: "tag_{0}".format(n))
